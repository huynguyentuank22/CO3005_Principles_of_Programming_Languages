.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [[F from Label2 to Label3
	iconst_2
	anewarray [F
	dup
	iconst_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 3.3
	fastore
	dup
	iconst_1
	ldc 4.4
	fastore
	aastore
	astore_1
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
Label10:
.var 3 is j I from Label10 to Label11
	iconst_0
	istore_3
Label12:
	iload_3
	iconst_2
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
Label18:
	aload_1
	iload_2
	aaload
	iload_3
	faload
	invokestatic io/putFloat(F)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label19:
Label14:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label12
Label15:
Label13:
	ldc ""
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label11:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label7:
Label5:
Label3:
Label1:
	return
.limit stack 17
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
