.source A.java
.class public A
.super java/lang/Object
.field x I
.field y F
.field z Z
.field s LGoString;
.field arr [I
.field b LA;

.method public <init>()V
.var 0 is this LA; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public foo()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/x I
	invokestatic io/putInt(I)V
	aload_0
	getfield A/y F
	invokestatic io/putFloat(F)V
	aload_0
	getfield A/s LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_0
	getfield A/z Z
	invokestatic io/putBool(Z)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public initarr(I)V
.var 0 is this LA; from Label0 to Label1
.var 1 is val I from Label0 to Label1
Label0:
Label2:
	aload_0
	iconst_5
	newarray int
	dup
	iconst_0
	iload_1
	iastore
	dup
	iconst_1
	iload_1
	iastore
	dup
	iconst_2
	iload_1
	iastore
	dup
	iconst_3
	iload_1
	iastore
	dup
	iconst_4
	iload_1
	iastore

	putfield A/arr [I
Label3:
Label1:
	return
.limit stack 12
.limit locals 2
.end method

.method public printArr()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_0
	istore_1
Label8:
	iload_1
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label12:
	aload_0
	getfield A/arr [I
	iload_1
	iaload
	invokestatic io/putInt(I)V
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 8
.limit locals 2
.end method

.method public testB()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield A/b LA;
	invokevirtual A/foo()V
	aload_0
	getfield A/b LA;
	bipush 6
	invokevirtual A/initarr(I)V
	aload_0
	getfield A/b LA;
	invokevirtual A/printArr()V
Label3:
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public initB()V
.var 0 is this LA; from Label0 to Label1
Label0:
Label2:
	aload_0
	iconst_1
	iconst_1
	new GoString
	dup
	ldc "kakaka"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/initA(IZLGoString;)LA;

	putfield A/b LA;
Label3:
Label1:
	return
.limit stack 6
.limit locals 1
.end method
