.source Person.java
.class public Person
.super java/lang/Object
.field name LGoString;
.field age I

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

.method public greet()LGoString;
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/name LGoString;
	invokestatic MiniGoClass/getGreeting(LGoString;)LGoString;
	areturn
Label3:
Label1:
.limit stack 1
.limit locals 1
.end method
