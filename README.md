## JMeter API

 Проект создан для нужд инженеров нагрузочного тестирования и позволяет собрать тесты на основе пустого тестплана созданного в JMeter (фаила .jmx) использую Python


## Возможности
Данный проект позволяет собрать тестплан точно такой же какой вы бы могли сделать в GUI JMeter
Все названия одинаковы с названиями компонетов в самом Jmeter

* Assertions  
* Configuration Elements
  + HTTP Cookie Manager
  + HTTP Cache Manager
  + HTTP Header Manager
  + HTTP Request Defaults
  + CSV Data Set Config
* Listeners
  + View result tree
  + Summery report
  + Backend listener
* Post processors
* Pre processors
* Samlers
* Test fragment
* Treads group
* Timers

Подробней об этих элементах Вам ни кто лучше не рассскажет, чем их разработчик [JMeter](https://jmeter.apache.org/usermanual/component_reference.html)
Это далеко не все возможность которые которые все время пополняются

 ## Как установить ?
 Это очень просто Вам ничего не потребуется, кроме выполнения простой команды в Вашем виртуальном окружении. JMeter API отлично работает как в Windows так и на Linux и им подобных системах

 ```
 user@name:~$ pip install jmeter-api
 ```
## Как пользоваться ?

После установки скачайте или перекопируйте себе фаил отсуда -> [example.py](https://github.com/lanitgithub/jmeter_api/blob/master/example_testplan_01.py) в директорию с установленным окружением и выполните

 ```
 user@name:~$ python3 example.py
 ```
 В том же расположении у Вас появится готовый тестплан

## Как быстро вникнуть ?

Мы всегда рады Вашей помошь и будем рады принять от Вас pull Request, если он пройдет все тесты    
Быстро разобраться вам поможет:    
* [Структура проекта](https://github.com/lanitgithub/jmeter_api/wiki)    
* [Документация]()

## Что реализовано ?

| номер | тип элемента | имя элемента | добавлен |    
|-------|--------------|--------------|----------|    
| 1 | assertions | json | + |
| 2 | assertions | jsr223 | + |    
| 3 | assertions | response | + |    
| 4 | assertions | size | + |
| 5 | assertions | duration | + |
| 6 | assertions | Response Assertion | - |
| 7 | assertions | XPath2 | - |
| 8 | assertions | Compare | - |
| 9 | assertions | HTML | - |
| 10 | assertions | JSON JMESPath | - |
| 11 | assertions | XML | - |
| 12 | assertions | XML Schema | - |
| 13 | assertions | BeanShell | - |    
||||   
| 14 | configs | counter | + |
| 15 | configs | csv_data_set_config | + |
| 16 | configs | http_auth_manager | + |
| 17 | configs | http_cache_manager | + |
| 18 | configs | http_cookie_manager | + |
| 19 | configs | http_header_manager | + |
| 20 | configs | http_request_defaults | + |
| 21 | configs | random_csv_data_set_config | + |
| 22 | configs | random_variable | + |
| 23 | configs | TCP Sampler | - |
| 24 | configs | Bolt Connection | - |
| 25 | configs | Simple Element | - |
| 26 | configs | Keystore | - |
| 27 | configs | LDAP Request Defaults | - |
| 28 | configs | LDAP Extended Request Defaults | - |
||||
| 29 | controllers | if_controller | + |
| 30 | controllers | include_controller | + |
| 31 | controllers | interleave_controller | + |
| 32 | controllers | loop_controller | + |
| 33 | controllers | module_controller | + |
| 34 | controllers | once_only_controller | + |
| 35 | controllers | random_controller | + |
| 36 | controllers | simple_controller | + |
| 37 | controllers | switch_controller | + |
| 38 | controllers | throughput_controller | + |
| 39 | controllers | transaction_controller | + |
| 40 | controllers | Runtime Controller | - |
| 41 | controllers | Recording Controller | - |
| 42 | controllers | Random Order Controller | - |
| 43 | controllers | ForEach Controller | - |
||||
| 44 | listeners | aggregate_report | + |
| 45 | listeners | backend | + |
| 46 | listeners | simple_data_writer | + |
| 47 | listeners | summary_report | + |
| 48 | listeners | view_results_tree | + |
| 49 | listeners | Aggregate Graph | - |
| 50 | listeners | Assertion Results | - |
| 51 | listeners | Comparison Assertion Visualizer | - |
| 52 | listeners | Generate Summary Results | - |
| 53 | listeners | Graph Results | - |
| 54 | listeners | JSR223 Listener | - |
| 55 | listeners | Mailer Visualizer | - |
| 56 | listeners | Response Time Graph | - |
| 57 | listeners | Save Responses to a file | - |
| 58 | listeners | View Result Tree Http2 | - |
| 59 | listeners | View Results in Table | - |
| 60 | listeners | BeanShell Listener | - |
||||
| 61 | non_test_elements | test_plan | + |
||||
| 62 | post_processors | debug | + |
| 63 | post_processors | json_extractor | + |
| 64 | post_processors | jsr223 | + |
| 65 | post_processors | CSS Selector Extractor | - |
| 66 | post_processors | JSON JMESPath Extractor | - |
| 67 | post_processors | Boundary Extractor | - |
| 68 | post_processors | JDBC PostProcessor | - |
| 69 | post_processors | Result Status Action Handler | - |
| 70 | post_processors | XPath Extractor | - |
| 71 | post_processors | XPath2 Extractor | - |
| 72 | post_processors | BeanShell PostProcessor | - |
||||
| 73 | pre_processors | jsr223 | + |
| 74 | pre_processors | User Parameters | - |
| 75 | pre_processors | HTML Link Parser | - |
| 76 | pre_processors | HTTP URL Re-writing Modifier | - |
| 77 | pre_processors | JDBC PreProcessor | - |
| 78 | pre_processors | RegEx User Parameters | - |
| 79 | pre_processors | Sample Timeout | - |
||||
| 80 | samplers | beanshell | + |
| 81 | samplers | debug | + |
| 82 | samplers | flow_control | + |
| 83 | samplers | http_request | + |
| 84 | samplers | jdbc_request | + |
| 85 | samplers | jsr223 | + |
| 86 | samplers | AJP/1.3 Sampler | - |
| 87 | samplers | Access Log Sampler | - |
| 88 | samplers | Bolt Request | - |
| 89 | samplers | FTP Request | - |
| 90 | samplers | TCP Sampler | - |
| 91 | samplers | HTTP2 Request | - |
| 92 | samplers | JMS Point-to-Point | - |
| 93 | samplers | JMS Publisher | - |
| 94 | samplers | JMS Subscriber | - |
| 95 | samplers | JUnit Request | - |
| 96 | samplers | Java Request | - |
| 97 | samplers | LDAP Extended Request | - |
| 98 | samplers | LDAP Request | - |
| 99 | samplers | Mail Reader Sampler | - |
| 100 | samplers | OS Process Sampler | - |
| 101 | samplers | SMTP Sampler | - |
| 102 | samplers | Dummy Sampler | - |
| 103 | samplers | HTTP Raw Request | - |
||||
| 104 | test_fragment | test_fragment | + |
||||
| 105 | thread_groups | arrivals_thread_group | + |
| 106 | thread_groups | common_thread_group | + |
| 107 | thread_groups | concurrency_thread_group | + |
| 108 | thread_groups | free_form_arrivals_thread_group | + |
| 109 | thread_groups | stepping_thread_group | + |
| 110 | thread_groups | teardown_thread_group | + |
| 111 | thread_groups | ultimate_thread_group | + |
||||
| 112 | timers | constant_throughput_timer | + |
| 113 | timers | constant_timer | + |
| 114 | timers | Precise Throughput Timer | - |
| 115 | timers | Gaussian Random Timer | - |
| 116 | timers | JSR223 Timer | - |
| 117 | timers | Poisson Random Timer | - |
| 118 | timers | Synchronizing Timer | - |
| 119 | timers | BeanShell Timer | - |


## Licence

 Copyright 2019 Aleksey Svetlov

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       https://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
   
