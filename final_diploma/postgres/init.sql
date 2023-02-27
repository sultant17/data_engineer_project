CREATE TABLE ga_sessions (
  session_id varchar(100) NOT NULL,
  client_id varchar(100) NOT NULL,
  visit_date date,
  visit_time time,
  visit_number INT,
  utm_source varchar(100),
  utm_medium varchar(100),
  utm_campaign varchar(100),
  utm_adcontent varchar(100),
  utm_keyword varchar(100),
  device_category varchar(100),
  device_os varchar(100),
  device_brand varchar(100),
  device_model varchar(100),
  device_screen_resolution varchar(100),
  device_browser varchar(100),
  geo_country varchar(100),
  geo_city varchar(100),
  PRIMARY KEY (session_id)
);


CREATE TABLE ga_hits (
  session_id varchar(100) NOT NULL REFERENCES ga_sessions,
  hit_date date,
  hit_time INT,
  hit_number INT NOT NULL,
  hit_type varchar(100),
  hit_referer varchar(100),
  hit_page_path varchar(3000),
  event_category varchar(100),
  event_action varchar(100),
  event_label varchar(100),
  event_value FLOAT(32),
  PRIMARY KEY (session_id, hit_number)
);


