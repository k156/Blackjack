# Blackjack

프로젝트 설명
------------
블랙잭 게임을 간단하게 파이썬으로 구현했습니다. 


게임룰
----------
카드를 받아 숫자의 합이 21에 가까운 쪽이 승리하는 게임.
 Computer = Dealer
 사용자 = Player
 52개의 카드에서 랜덤한 2장이 딜러와 플레이어에게 주어집니다.
 A카드의 경우 1과 11중에 선택할 수 있습니다.
 J,Q,K는 10으로 계산됩니다.
 플레이어는 Hit과 Stand 중에 선택할 수 있습니다.
 Hit을 선택할 경우 카드를 한 장 더 받습니다.
 Stand를 선택할 경우 카드를 그만 받게 됩니다.
 딜러는 17보다 작은 경우에만 카드가 추가됩니다.
 21을 초과하면 패, 21일 경우 승.


Collaborator
-------------
이현주 (Player class, Dealer class, main flow),
김정민 (Game class, main flow)


설치 및 사용법
----------------
Git bash를 실행시킨 후
git clone https://github.com/k156/Blackjack.git


모듈
--------------
import random 

from functools import reduce

import os
