.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static isPrime(I)Z
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	iconst_0
	ireturn
Label10:
Label6:
Label7:
Label13:
.var 1 is i I from Label13 to Label14
	iconst_2
	istore_1
Label15:
	iload_1
	iload_1
	imul
	iload_0
	if_icmpgt Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label12
	goto Label16
Label11:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label15
Label16:
Label19:
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
Label25:
Label26:
	iconst_0
	ireturn
Label27:
Label23:
Label24:
Label20:
	goto Label11
Label12:
Label14:
	iconst_1
	ireturn
Label3:
Label1:
.limit stack 12
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	bipush 17
	invokestatic MiniGoClass/isPrime(I)Z
	invokestatic io/putBoolLn(Z)V
	bipush 15
	invokestatic MiniGoClass/isPrime(I)Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 1
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
