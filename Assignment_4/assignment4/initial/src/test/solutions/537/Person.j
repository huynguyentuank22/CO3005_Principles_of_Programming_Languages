.source Person.java
.class public Person
.super java/lang/Object
.implements AI
.field name LString_MiniGo;
.field age I
.field cars [LCar;

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

.method public print()V
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
	getfield Person/cars [LCar;
	iconst_0
	aaload
	invokevirtual Car/print()V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public changed()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
 	getfield Person/name LString_MiniGo;

	new String_MiniGo
	dup
	ldc "Peter"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V

	invokevirtual String_MiniGo/getValue()Ljava/lang/String;

	invokevirtual String_MiniGo/setValue(Ljava/lang/String;)V

	aload_0
	bipush 81

	putfield Person/age I
	aload_0
	getfield Person/cars [LCar;
	iconst_0
	aaload
	invokevirtual Car/changed()V
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public getCar()LCar;
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/cars [LCar;
	iconst_0
	aaload
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
