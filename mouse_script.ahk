#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force
#Persistent




hk(keyboard:=0, mouse:=0, message:="", timeout:=3) { 
   static AllKeys
   if !AllKeys {
      s := "||NumpadEnter|Home|End|PgUp|PgDn|Left|Right|Up|Down|Del|Ins|"
      Loop, 254
         k := GetKeyName(Format("VK{:0X}", A_Index))
       , s .= InStr(s, "|" k "|") ? "" : k "|"
      For k,v in {Control:"Ctrl",Escape:"Esc"}
         AllKeys := StrReplace(s, k, v)
      AllKeys := StrSplit(Trim(AllKeys, "|"), "|")
   }
   ;------------------
   For k,v in AllKeys {
      IsMouseButton := Instr(v, "Wheel") || Instr(v, "Button")
      Hotkey, *%v%, Block_Input, %  (mouse && IsMouseButton) ? "On" : "Off"
   }
   if (message != "") {
      Progress, B1 M FS12 ZH0, %message%
      SetTimer, TimeoutTimer, % -timeout*1000
   }
   else
      Progress, Off
   Block_Input:
   Return
   TimeoutTimer:
   Progress, Off
   Return
}

NumpadDiv::hk(1,1,"")   ; Disable all keyboard keys and mouse buttons with Numpad-Div "/"
NumpadMult::hk(0,0,"")         ; Enable all keyboard keys and mouse buttons with Numpad-Mult "*"
NumpadSub::ExitApp  ; Exit Script with Numpad-Minus "-"