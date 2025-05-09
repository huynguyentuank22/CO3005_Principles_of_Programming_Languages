.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
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
	getstatic MiniGoClass/arr [I
	iload_1
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
Label19:
	getstatic MiniGoClass/arr [I
	iload_1
	iaload
	invokestatic io/putInt(I)V
Label20:
Label16:
Label17:
Label13:
	goto Label4
Label5:
Label7:
Label23:
.var 2 is i I from Label23 to Label24
	iconst_0
	istore_2
Label25:
	iload_2
	iconst_5
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
	getstatic MiniGoClass/arr [I
	iload_2
	iaload
	iconst_2
	irem
	iconst_0
	if_icmpeq Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label33
Label35:
Label36:
	getstatic MiniGoClass/arr [I
	iload_2
	iaload
	invokestatic io/putInt(I)V
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
.limit stack 22
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
	iconst_5
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
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	putstatic MiniGoClass/arr [I
Label0:
Label1:
	return
.limit stack 16
.limit locals 0
.end method
