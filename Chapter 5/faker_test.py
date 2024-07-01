"""
prompt> py --version #python version 확인
prompt> py -m pip --version #pip 버전 확인
prompt> py -m pip install [install할 Package Name] #pip를 이용한 패키지 설치
"""

from faker import Faker

fake = Faker('ko-KR')

print(fake.name())
print(fake.address())

print('\n\n')

test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)

print(type(test_data)) # list