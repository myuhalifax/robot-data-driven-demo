*** Settings ***
Resource    ../resources/common.robot

*** Test Cases ***
Clean Run Has No Errors In Log
    ${outdir}=    Run Data Set And Check Counts    mixed.csv    run_logcheck    1    1    1
    ${log}=    Read Log    ${outdir}
    Should Not Contain    ${log}    ERROR

Bad Data Produces Error Evidence In Log
    ${outdir}=    Run Data Set And Check Counts    badrow.csv    run_logbad    1    0    0
    ${log}=    Read Log    ${outdir}
    Should Contain    ${log}    ERROR bad row skipped

Empty Run Warns About No Contacts
    ${outdir}=    Run Data Set And Check Counts    empty.csv    run_logempty    0    0    0
    ${log}=    Read Log    ${outdir}
    Should Contain    ${log}    WARN no contacts detected

Missing Input File Fails Cleanly
    Run Keyword And Expect Error    *    Run Processor    no_such_file.csv    run_missing
