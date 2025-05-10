.source Person.java
.class public Person
.super java/lang/Object
.field name LString_MiniGo;
.field age I
.field height F
.field car LCar;

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public bar()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/name LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Person/age I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Person/height F
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield Person/car LCar;
	invokevirtual Car/print()V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
