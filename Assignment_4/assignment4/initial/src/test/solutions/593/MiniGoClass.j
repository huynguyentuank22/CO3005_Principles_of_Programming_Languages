.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static reverseArray([I)[I
.var 0 is arr [I from Label0 to Label1
Label0:
Label2:
.var 1 is result [I from Label2 to Label3
	iconst_3
	newarray int
	astore_1
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	iconst_3
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
	aload_0
	iconst_2
	iload_2
	isub
	iaload
	iastore
Label13:
	goto Label4
Label5:
Label7:
	aload_1
	areturn
Label3:
Label1:
.limit stack 10
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is arr [I from Label2 to Label3
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	astore_1
.var 2 is reversed [I from Label2 to Label3
	aload_1
	invokestatic MiniGoClass/reverseArray([I)[I
	astore_2
	aload_2
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
	aload_2
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
	aload_2
	iconst_2
	iaload
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 14
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
