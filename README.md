# Home Assistant Zigbee RS-485 Electricity Meters Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)


This is Home Assistant custom integration for obtaining the data from Electricity Meters with RS-485 port over Zigbee.

Because I have meters, manufactured in Russia only, I'm sure than this integration is dedicated for Russia users only. 
BTW, if you need documentation in English, you can use [Google Translate](https://translate.google.com)

### This is a Alpha version!
### Работа только начата - оформление репозитория, сама интеграция и модем находится в глубокой разработке


Интеграция для получения показаний со счетчиков электроэнергии с интерфейсом RS-485, передача с помощью Zigbee и отображение в Home Assistant.

Вдохновлен впечатляющим результатом [@MenshikovDmitry](https://github.com/MenshikovDmitry/ha-mercury-200-integration)

Первыми будут появляться счетчики Меркурий в силу своей распространенности (и физического наличия их у меня).


***ВНИМАНИЕ!!! Высокое напряжение! Опасно для жизни!***

Модем для своей работы требует подключение к сети 220V, поэтому сборку и подключение должны выполнять профессионалы!

_*Автор разработки не несет ответственности за возможные последствия корректного и некорректного подключения и использования материалов данного репозитория!*_

## Введение

Многие бытовые счетчики электроэнергии (такие как __Меркурий 200.02__, __Меркурий 230 ART-01 CN__) обладают цифровым интерфейсом на базе __RS-485__, который предназначен для взаимодействия со счетчиком (чтение параметров, значений потребления, конфигурирование).

Данный репозиторий содержит:
- интеграцию с HACS для отображения показаний потребления в Home Assistant через [zigbee2mqtt](https://www.zigbee2mqtt.io) ~~или [SLS Gateway](https://slsys.github.io/Gateway/) (временно не работает)~~
- информацию для сборки модема в типоразмере 1-DIN для монтажа на рейку внутри элетрического шкафа.


## Возможности

[[todo]]

## Установка

### Через [HACS](https://hacs.xyz/) (рекомендуется)
_Раздел в разработке_  
Добавьте ссылку на этот репозиторий в HACS и Установите компонент.

### Вручную (не рекомендуется)

[[todo]]

## Настройка

[[todo]]

## Использование
[[todo]]

## Модем Zigbee-RS485
[[todo]]

## TODO:

```diff
- оформить репозиторий, выложить наработки
- модем для монтажа на рейку размером 1-DIN
- реализация для счетчика Меркурий 200.02 
- реализация для счетчика Меркурий 230 ART-01 CN
```

## Полезные ссылки 
* Основная идея [@MenshikovDmitry](https://github.com/MenshikovDmitry/ha-mercury-200-integration) - ему основная благодарность за направление с модемом!
* [Расшифровка протокола Mercury 200](https://github.com/mrkrasser/MercuryStats) 
* [Протокол счетчиков Меркурий 3 фазы](https://www.incotexcom.ru/files/em/docs/merkuriy-sistema-komand-ver-1-2021-12-24.pdf)
* [Протокол счетчиков Меркурий 1 фаза](https://www.incotexcom.ru/files/em/docs/mercury-protocol-obmena-1.pdf)
* [Cкрипт на питоне для чтения данных из Mercury 203.2T через RS-485](https://github.com/n0l/Mercury_remote/blob/master/get_data_python3.py)

**Спасибо Авторам!**
