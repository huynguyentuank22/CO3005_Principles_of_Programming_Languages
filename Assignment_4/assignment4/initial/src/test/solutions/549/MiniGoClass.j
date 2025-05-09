.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	bipush 10
	invokestatic MiniGoClass/foo(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(I)V
.var 0 is n I from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_1
	istore_1
Label8:
	iload_1
	iload_0
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
	iload_1
	invokestatic io/putInt(I)V
Label13:
	goto Label4
Label5:
Label7:
Label16:
.var 2 is i I from Label16 to Label17
	iconst_1
	istore_2
Label18:
	iload_2
	iload_0
	if_icmpge Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label15
	goto Label19
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label18
Label19:
Label22:
	iload_2
	invokestatic io/putInt(I)V
Label23:
	goto Label14
Label15:
Label17:
Label3:
Label1:
	return
.limit stack 11
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label24:
Label25:
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
