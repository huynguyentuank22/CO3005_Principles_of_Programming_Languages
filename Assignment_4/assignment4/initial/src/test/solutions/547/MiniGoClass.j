.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I
.field static b I
.field static c F
.field static d F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
Label15:
Label16:
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	iadd
	invokestatic io/putIntLn(I)V
Label17:
Label13:
Label14:
Label10:
	goto Label7
Label6:
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	imul
	bipush 18
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
Label22:
Label23:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fadd
	invokestatic io/putFloatLn(F)V
Label24:
	goto Label21
Label20:
Label25:
Label26:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fsub
	invokestatic io/putFloatLn(F)V
Label27:
Label21:
Label7:
Label3:
Label1:
	return
.limit stack 9
.limit locals 1
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
	iconst_1
	invokestatic MiniGoClass/foo()I
	iadd
	iconst_2
	iadd
	putstatic MiniGoClass/a I
	iconst_3
	putstatic MiniGoClass/b I
	ldc 4.0
	putstatic MiniGoClass/c F
	ldc 6.0
	putstatic MiniGoClass/d F
Label0:
Label1:
	return
.limit stack 4
.limit locals 0
.end method
