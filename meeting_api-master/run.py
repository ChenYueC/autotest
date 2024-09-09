import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    # os.system(r'copy environment.properties .\report\environment.properties')
    os.popen(r'copy environment.properties .\tmp_report\environment.properties')
    os.system('allure generate ./tmp_report -o ./report --clean')
