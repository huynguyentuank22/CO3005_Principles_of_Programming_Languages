.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final a I
.field static y F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/y F
	bipush 16
	i2f
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	invokestatic io/putInt(I)V
Label10:
	goto Label7
Label6:
Label11:
Label12:
	getstatic MiniGoClass/a I
	bipush 10
	iadd
	sipush 211
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
Label19:
	sipush 234
	invokestatic io/putIntLn(I)V
Label20:
	goto Label17
Label16:
Label21:
Label22:
.var 1 is x I from Label22 to Label23
	iconst_5
	istore_1
Label24:
	iload_1
	bipush 10
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label25
Label28:
	sipush 567
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label29:
	goto Label24
Label25:
Label23:
Label17:
	getstatic MiniGoClass/a I
	invokestatic MiniGoClass/foo()I
	iadd
	iconst_1
	iadd
	invokestatic io/putInt(I)V
Label13:
Label7:
Label32:
.var 1 is i I from Label32 to Label33
	iconst_0
	istore_1
Label34:
	iload_1
	bipush 10
	if_icmpge Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	ifle Label31
	goto Label35
Label30:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label34
Label35:
Label38:
	iload_1
	invokestatic io/putInt(I)V
Label39:
	goto Label30
Label31:
Label33:
Label3:
Label1:
	return
.limit stack 23
.limit locals 2
.end method

.method public static foo()I
Label0:
Label2:
	iconst_1
	iconst_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 0
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
	bipush 20
	bipush 10
	imul
	putstatic MiniGoClass/a I
	ldc 15.5
	putstatic MiniGoClass/y F
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
