# ITGC-03 - Change Management Test

$data = Import-Csv .\evidence\change_management.csv

$total = $data.Count

$exceptions = @(
    $data | Where-Object {
        $_.Approval -eq "No" -or
        $_.Testing_Evidence -eq "No" -or
        $_.Implementation_Documented -eq "No"
    }
)

$passed = $total - $exceptions.Count
$exceptionCount = $exceptions.Count

Write-Host ""
Write-Host "ITGC-03 CHANGE MANAGEMENT TEST"
Write-Host "-------------------------------"
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
        Format-Table Change_ID, System, Description, Approval, Testing_Evidence, Implementation_Documented
}