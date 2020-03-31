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
* [Структура проекта]()    
* [Документация]()

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
