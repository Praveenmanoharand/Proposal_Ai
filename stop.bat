@echo off
echo Stopping ProposeAI Application on port 5000...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000') do (
    taskkill /f /pid %%a
    echo Process %%a terminated.
)
echo Application stopped.
echo Application stopped.
