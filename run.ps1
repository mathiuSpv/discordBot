$currentPath = (Get-Location).Path

cd $currentPath

try {
    .\venv\Scripts\Activate #activate venv
} catch {
    Write-Host "Installing virtual environment..." -ForegroundColor Yellow
    py -m venv venv #create venv
    .\venv\Scripts\Activate #activate venv
} finally {
    Write-Host  "Virtual environment activated." -ForegroundColor Green
}

#libraries installers.
try {
    if(Test-Path -Path  "requirements.txt") {
        $libraries = Get-Content -Path "requirements.txt"
    } else {
        throw "No requirements.txt file found."
    }
    $needInstalled = $false
    foreach ($library in $libraries) {
        $packageName = $library.Split("==")[0]
        $result = & pip show $packageName 2>&1
        if ($result -match "WARNING: Package\(s\) not found.") {  #if package is not installed
            $needInstalled = $true
            Write-Host  "Installing Packages needed..." -ForegroundColor Yellow
            pip install -r requirements.txt > $null
            Write-Host   "Packages installed." -ForegroundColor Green
            break
        }
    }
    if (!$needInstalled){ # if not run command pip install 
        Write-Host "Packages was already installed." -ForegroundColor Green
    }
} catch {
    Write-Host "$_" -ForegroundColor Red
}