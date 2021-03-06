<?php

if (preg_match("/base\.php$/", $_SERVER['PHP_SELF'])){
	exit('No direct script access allowed');
}

class Base {

  public $http_code; /* Last HTTP status code | @var string */
  public $url;  /* Last API call | @var string */
  public $host = "https://hyperpublic.com/api/v1"; /* Hyperpublic API base URL | @var string */
  public $timeout = 30; /* Timeout default | @var integer */
  public $connect_timeout = 30; /* Connect timeout default | @var integer */
  public $http_info; /* Lat HTTP headers | @var string */
  public $useragent = "Hyperpublic PHP beta"; /* Useragent string | @var string */
  public $ssl_verifypeer = FALSE; /* Verify SSL Cert? | @var boolean */

  /**
   * Make an HTTP GET request
   *
   */    
  public function get($url = ''){
    $url = $this->host . $url;
    $response = $this->http($url, 'GET');
    $response = json_decode($response);
    if (isset($response)){
      foreach ($response as $key => $value) {
        $this->{$key} = $value;
      }
      return $this;
    } else {
      return FALSE;
    }
  }

  /**
   * Make an HTPP POST request
   *
   */      
  public function post($url = '') {
    $url = $this->host . $url;
    $response = $this->http($url, 'POST');
    $response = json_decode($response);
    if (isset($response)){
      foreach ($response as $key => $value) {
        $this->{$key} = $value;    
      }
      return $this;       
    } else {
      return FALSE;
    }
  }
    
  /**
   * Make an HTTP request
   *
   * @return API results
   */
  function http($url = '', $method = '', $post_fields = NULL) {
    $this->http_info = array();
    $ci = curl_init();
    /* Curl settings */
    curl_setopt($ci, CURLOPT_USERAGENT, $this->useragent);
    curl_setopt($ci, CURLOPT_CONNECTTIMEOUT, $this->connect_timeout);
    curl_setopt($ci, CURLOPT_TIMEOUT, $this->timeout);
    curl_setopt($ci, CURLOPT_RETURNTRANSFER, TRUE);
    curl_setopt($ci, CURLOPT_HTTPHEADER, array('Expect:'));
    curl_setopt($ci, CURLOPT_SSL_VERIFYPEER, $this->ssl_verifypeer);
    curl_setopt($ci, CURLOPT_HEADERFUNCTION, array($this, 'getHeader'));
    curl_setopt($ci, CURLOPT_HEADER, FALSE);

    switch ($method) {
    case 'POST':
      curl_setopt($ci, CURLOPT_POST, TRUE);
      if (!empty($post_fields)) {
        curl_setopt($ci, CURLOPT_POST_FIELDS, $post_fields);
      }
      break;
    case 'DELETE':
      curl_setopt($ci, CURLOPT_CUSTOMREQUEST, 'DELETE');
      if (!empty($post_fields)) {
        $url = "{$url}?{$post_fields}";
      }
    }

    curl_setopt($ci, CURLOPT_URL, $url);
    $response = curl_exec($ci);
    $this->http_code = curl_getinfo($ci, CURLINFO_HTTP_CODE);
    $this->http_info = array_merge($this->http_info, curl_getinfo($ci));
    $this->url = $url;
    curl_close ($ci);
    return $response;
  }

  /**
   * Get the header info to store.
   */
  function getHeader($ch, $header) {
    $i = strpos($header, ':');
    if (!empty($i)) {
      $key = str_replace('-', '_', strtolower(substr($header, 0, $i)));
      $value = trim(substr($header, $i + 2));
      $this->http_header[$key] = $value;
    }
    return strlen($header);
  }

}