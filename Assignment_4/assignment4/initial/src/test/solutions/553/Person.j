.source Person.java
.class public Person
.super java.lang.Object
.field public name Ljava/lang/String;
.field public age I

.method public <init>(Ljava/lang/String;I)V
Label0:
.var 0 is this LPerson; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LPerson; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
	aload_0
	ldc ""
	putfield Person/name Ljava/lang/String;
	aload_0
	iconst_0
	putfield Person/age I
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public averageAge(LPerson;)I
Label0:
.var 0 is this LPerson; from Label0 to Label1
.var 1 is p1 LPerson; from Label0 to Label1
Label2:
	aload_0
	getfield Person/age I
	aload_1
	getfield Person/age I
	iadd
	iconst_2
	idiv
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 2
.end method
