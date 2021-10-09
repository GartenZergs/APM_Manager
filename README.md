# APM_Manager
This script restricts your APM in the game Starcraft II

## How to use it?
1. Download the latest version of the APM-Manager (RAR-File under "Releases")
2. Unzip the APM-Manager folder anywhere
3. Inside the folder run these files in this order:
    `RUN_AHK.bat` and `RUN_APMManager.bat`

4. If you want to exit the program: Press `-` on the Numpad.

## Settings
The default APM-Cap is set to 120, but you can change it.
Inside `settings.ini` you should see the variables
`actions=x` and `seconds=y`.
The script will allow you to execute at most `x`actions in `y` seconds. So for example if:
`actions=4` and `seconds=3`, you will be able to execute at most 4 keypresses or mouseclicks combined in 3 seconds. The APM is calculated with
`APM=actions/seconds*60` , therefore it would be 80APM in this example.
