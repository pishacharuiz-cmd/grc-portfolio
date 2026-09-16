# ITGC-02 — Privileged Access Management Test

$data = Import-Csv .\evidence\privileged_access.csv

$total = $data.Count

$privileged = @(
    $data | Where-Object {
        $_.Admin_Access -eq "Yes"
    }
)

$exceptions = @(
    $privileged | Where-Object {
        $_.Business_Justification -eq "No"
    }
)

$privilegedCount = $privileged.Count
$exceptionCount = $exceptions.Count

Write-Host ""
Write-Host "ITGC-02 PRIVILEGED ACCESS MANAGEMENT TEST"
Write-Host "------------------------------------------"
Write-Host "Records Tested: $total"
Write-Host "Privileged Accounts: $privilegedCount"
Write-Host "Exceptions: $exceptionCount"

if ($exceptionCount -eq 0) {
    Write-Host "CONTROL RESULT: PASS"
}
else {
    Write-Host "CONTROL RESULT: EXCEPTION"
    Write-Host ""
    Write-Host "Exceptions Identified:"
    
    $exceptions |
        Format-Table User, Role, Department, Admin_Access, Business_Justification
}