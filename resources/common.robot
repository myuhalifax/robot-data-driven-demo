*** Settings ***
Library    ../libraries/ProcessorLibrary.py

*** Keywords ***
Run Data Set And Check Counts
    [Arguments]    ${data_file}    ${run_name}    ${contacts}    ${weak}    ${noise}
    ${outdir}=    Run Processor    ${data_file}    ${run_name}
    ${summary}=    Read Summary    ${outdir}
    Should Be Equal As Integers    ${summary}[CONTACT]    ${contacts}
    Should Be Equal As Integers    ${summary}[WEAK]       ${weak}
    Should Be Equal As Integers    ${summary}[NOISE]      ${noise}
    [Return]    ${outdir}
