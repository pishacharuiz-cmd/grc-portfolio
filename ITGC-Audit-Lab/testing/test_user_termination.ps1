# ITGC-04 - User Termination Test

$data = Import-Csv .\evidence\user_termination.csv

$total = $data.Count

$exceptions = @(
    $data | Where-Object {
        $_.Termination_Date -ne $_.Account_Disabled_Date
    }
)

$passed = $total - $exceptions.Count
$exceptionCount = $exceptions.Count

Write-Host ""
Write-Host "ITGC-04 USER TERMINATION TEST"
Write-Host "------------------------------"
Write-Host "Records Tested: $total"
Write-Host "Passed: $passed"
Write-Host "Exceptions: $exceptionCount"

if ($exceptionCount -eq 0) {
    Write-Host "CONTROL RESULT: PASS"
}
else {
    Write-Host "CONTROL RESULT: EXCEPTION"
    Write-Host ""
    Write-Host "Exceptions Identified:"

    $exceptions |
        Format-Table Employee, Department, Termination_Date, Account_Disabled_Date, Result
}