@Echo off
Mode Con: lines=23 Cols=61
title Menu Batch - Usando CHOICE
color 03

:i
cls
Echo.
echo  ���������������������������������������������������������ͻ
echo  �                                                         �
echo  � Menu Marcelo Victor           		     ۲��  �
echo  �                                                         �
echo  ���������������������������������������������������������͹
echo  �                                                         �
echo  � Para iniciar um programa, digite seu numero:            �
echo  ���������������������������������������������������������͹
echo  �                                                         �
echo  � ���������������ͻ ���������������ͻ ����������������ͻ  �
echo  � ���������������͹ ���������������͹ ����������������͹  �
echo  � �1: Calculadora � �2: G. Tarefas  � �3: B. de notas  �  �
echo  � ���������������ͼ ���������������ͼ ����������������ͼ  �
echo  � ���������������ͻ ���������������ͻ ����������������ͻ  �
echo  � ���������������͹ ���������������͹ ����������������͹  �
echo  � �4: W. Update   � �5: Paint       � �6: I. Explorer  �  �
echo  � ���������������ͼ ���������������ͼ ����������������ͼ  �
echo  �                                                         �
echo  ���������������������������������������������������������ͼ
echo.
choice /c "123456"  /n /m "�Digite> "

:dec
echo Resultado: %errorlevel%
pause >nul
goto %errorlevel%

:1
start calc.exe
goto i
:2
start taskmgr.exe
goto i
:3
start notepad.exe
goto i
:4
start wuapp.exe
goto i
:5
start mspaint.exe
goto i
:6
start iexplore.exe
goto i