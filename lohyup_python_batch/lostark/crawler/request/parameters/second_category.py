from enum import Enum


class SecondCategory(Enum):
    """
    로스트아크 거래소 secondCategory Code
    """
    ALL = 0  # 전체
    """
    AVATAR 20000
    """
    WEAPON = 20005  # 무기
    HEAD = 20010  # 머리
    FACE1 = 20020  # 얼굴1
    FACE2 = 20030  # 얼굴2
    TOP = 20050  # 상의
    BOTTOM = 20060  # 하의
    TOP_BOTTOM_SET = 20070  # 상하의세트
    MUSICAL_INSTRUMENT = 21400  # 악기
    AVATAR_BOX = 21500  # 아바타상자

    """
    REINFORCE_MATERIAL 50000
    """
    REFINING_MATERIAL = 50010  # 재련재료
    ADDITIONAL_MATERIAL_FOR_REFINING = 50020  # 재련추가재료
    ETC_MATERIAL = 51000  # 기타재료

    """
    BATTLE_ITEM 60000
    """
    BATTLE_ITEM_RECOVERY_TYPE = 60200  # 배틀아이템 - 회복형
    BATTLE_ITEM_ATTACK_OFFENSIVE = 60300  # 배틀아이템 - 공격형
    BATTLE_ITEM_FUNCTIONAL = 60400  # 배틀아이템 - 기능성
    BATTLE_ITEM_BUFF_TYPE = 60500  # 배틀아이템 - 버프형

    """
    LIFE_MATERIAL 90000
    """
    PLANT_COLLECTION_LOOT = 90200  # 식물채집 전리품
    LOGGING_LOOT = 90300  # 벌목 전리품
    MINING_LOOT = 90400  # 채광전리품
    HUNTING_LOOT = 90500  # 수렵전리품
    FISHING_LOOT = 90600  # 낚시전리품
    ARCHAEOLOGY_LOOT = 90700  # 고고학전리품
    ETC_LOOT = 90800  # 기타전리품

    """
    SHIP_MATERIAL 110000
    """
    SHIP_MATERIAL = 110100  # 선박 재료
    SHIP_SKIN = 110110  # 선박 스킨
    SHIP_MATERIAL_BOX = 111900  # 선박 재료 상자

    """
    PET 140000
    """
    PET = 140100  # 펫
    PET_BOX = 140200  # 펫 상자

    """
    VEHICLE 160000
    """
    VEHICLE = 160100  # 탈 것
    VEHICLE_BOX = 160200  # 탈 것 상자
