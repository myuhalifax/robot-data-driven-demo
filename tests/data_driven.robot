*** Settings ***
Resource          ../resources/common.robot
Test Template     Run Data Set And Check Counts
Documentation     Data-driven: same steps, one row per data set.
...               Data lives in the case table; inputs live in data/ files.

*** Test Cases ***              DATA FILE          RUN NAME      CONTACTS  WEAK  NOISE
Strong contacts only            strong.csv         run_strong    3         0     0
Mixed signals                   mixed.csv          run_mixed     1         1     1
All noise                       noise.csv          run_noise     0         0     3
Bad row is logged not fatal     badrow.csv         run_badrow    1         0     0
