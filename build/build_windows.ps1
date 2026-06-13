# Build metroidprime2.apworld for Windows
# Run from the project root: .\build\build_windows.ps1

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SrcDir = "$ProjectRoot\src"
$OutDir = "$ProjectRoot\build\target"
$TempDir = "$OutDir\metroidprime2"
$OutFile = "$OutDir\metroidprime2.apworld"

# Clean up temp
if (Test-Path $TempDir) { Remove-Item -Recurse -Force $TempDir }
if (Test-Path $OutFile) { Remove-Item -Force $OutFile }
New-Item -ItemType Directory -Force $OutDir | Out-Null
New-Item -ItemType Directory -Force $TempDir | Out-Null

# Copy src/ into temp/metroidprime2/, excluding junk
$Exclude = @('.git', '__pycache__', 'build', 'LICENSE', 'README.md', 'requirements.txt', 'Metroid Prime 2 Echoes.yaml', '*.iso', 'test', 'lib')
Get-ChildItem -Path $SrcDir | Where-Object {
    $name = $_.Name
    -not ($Exclude | Where-Object { $name -like $_ })
} | ForEach-Object {
    if ($_.PSIsContainer) {
        Copy-Item -Path $_.FullName -Destination "$TempDir\$($_.Name)" -Recurse
    } else {
        Copy-Item -Path $_.FullName -Destination "$TempDir\$($_.Name)"
    }
}

# Remove __pycache__ from nested dirs
Get-ChildItem -Path $TempDir -Recurse -Filter "__pycache__" -Directory | Remove-Item -Recurse -Force

# Zip using Python so entries use forward-slash separators (Compress-Archive uses backslashes
# which breaks the apworld's zip path scanning on load)
$Python = "C:\Program Files\Maxon Cinema 4D 2025\resource\modules\python\libs\win64\python.exe"
$PyScript = @"
import zipfile, os
from zipfile import ZipInfo
base = r'$OutDir'
src = r'$TempDir'
out = r'$OutFile'
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        # Add directory entry with trailing slash (required by apworld loader to discover subdirs)
        dir_arc = os.path.relpath(root, base).replace(os.sep, '/') + '/'
        if dir_arc != './':
            zi = ZipInfo(dir_arc)
            zf.writestr(zi, '')
        for file in files:
            abs_path = os.path.join(root, file)
            arcname = os.path.relpath(abs_path, base).replace(os.sep, '/')
            zf.write(abs_path, arcname)
"@
& $Python -c $PyScript

# Clean up temp folder
Remove-Item -Recurse -Force $TempDir

Write-Host "Built: $OutFile" -ForegroundColor Green
