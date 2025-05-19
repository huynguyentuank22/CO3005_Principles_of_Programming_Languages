.source Person.java
.class public Person
.super java.lang.Object
.field public name Ljava/lang/String;
.field public age I
.field public address LAddress;

.method public <init>(Ljava/lang/String;ILAddress;)V
Label0:
.var 0 is this LPerson; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
.var 3 is address LAddress; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
	aload_0
	aload_3
	putfield Person/address LAddress;
Label3:
Label1:
	return
.limit stack 5
.limit locals 4
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
	aload_0
	new Address
	dup
	invokespecial Address/<init>()V
	putfield Person/address LAddress;
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
.end method
