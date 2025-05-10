.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static sumEvenIndices([I)I
.var 0 is arr [I from Label0 to Label1
Label0:
Label2:
.var 1 is sum I from Label2 to Label3
	iconst_0
	istore_1
Label6:
.var 2 is i I from Label6 to Label7
	iconst_0
	istore_2
Label8:
	iload_2
	iconst_4
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
	iconst_2
	iadd
	istore_2
	goto Label8
Label9:
Label12:
	iload_1
	aload_0
	iload_2
	iaload
	iadd
	istore_1
Label13:
	goto Label4
Label5:
Label7:
	iload_1
	ireturn
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
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 10
	iastore
	dup
	iconst_2
	bipush 15
	iastore
	dup
	iconst_3
	bipush 20
	iastore
	astore_1
	aload_1
	invokestatic MiniGoClass/sumEvenIndices([I)I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 13
.limit locals 2
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
