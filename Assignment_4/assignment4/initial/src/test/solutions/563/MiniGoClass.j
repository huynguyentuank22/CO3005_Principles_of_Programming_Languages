.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static foo([F)V
.var 0 is arr [F from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_0
	istore_1
Label8:
	iload_1
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
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label12:
	aload_0
	iload_1
	aload_0
	iload_1
	faload
	iconst_2
	i2f
	fmul
	fastore
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 9
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [F from Label2 to Label3
	getstatic MiniGoClass/MAX I
	newarray float
	astore_1
	getstatic MiniGoClass/MAX I
	newarray float
	dup
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	dup
	iconst_2
	ldc 3.0
	fastore
	dup
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_4
	ldc 5.0
	fastore
	astore_1
	aload_1
	invokestatic MiniGoClass/foo([F)V
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
	faload
	invokestatic io/putFloat(F)V
Label13:
	goto Label4
Label5:
Label7:
Label3:
Label1:
	return
.limit stack 29
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
	iconst_5
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
