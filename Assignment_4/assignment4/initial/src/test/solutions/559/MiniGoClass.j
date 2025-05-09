.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is arr [LA; from Label2 to Label3
	getstatic MiniGoClass/MAX I
	anewarray A
	astore_1
	getstatic MiniGoClass/MAX I
	anewarray A
	dup
	iconst_0
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_1
	putfield A/x I
	dup
	new B
	dup
	invokespecial B/<init>()V
	dup
	iconst_2
	putfield B/y I
	putfield A/b LB;
	aastore
	dup
	iconst_1
	new A
	dup
	invokespecial A/<init>()V
	dup
	iconst_3
	putfield A/x I
	dup
	new B
	dup
	invokespecial B/<init>()V
	dup
	iconst_4
	putfield B/y I
	putfield A/b LB;
	aastore
	astore_1
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	getstatic MiniGoClass/MAX I
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label5
	goto Label9
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
Label12:
	aload_1
	iload_2
	aaload
	invokevirtual A/foo()V
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 25
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label14:
Label15:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	iconst_2
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
