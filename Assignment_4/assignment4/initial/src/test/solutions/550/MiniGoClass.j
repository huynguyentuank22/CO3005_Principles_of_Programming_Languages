.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
Label6:
.var 1 is i I from Label6 to Label7
	iconst_1
	istore_1
Label8:
	iload_1
	bipush 10
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
	iconst_2
	irem
	iconst_0
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
Label19:
	goto Label4
Label20:
Label16:
Label17:
	iload_1
	invokestatic io/putInt(I)V
Label13:
	goto Label4
Label5:
Label7:
Label23:
.var 2 is i I from Label23 to Label24
	iconst_1
	istore_2
Label25:
	iload_2
	bipush 10
	if_icmpge Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifle Label22
	goto Label26
Label21:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label25
Label26:
Label29:
	iload_2
	invokestatic io/putInt(I)V
	iload_2
	bipush 7
	if_icmpne Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label33
Label35:
Label36:
	goto Label22
Label37:
Label33:
Label34:
Label30:
	goto Label21
Label22:
Label24:
Label3:
Label1:
	return
.limit stack 20
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label38:
Label39:
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
