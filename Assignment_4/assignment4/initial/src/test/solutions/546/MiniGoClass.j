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
	getstatic MiniGoClass/a I
	getstatic MiniGoClass/b I
	if_icmpge Label4
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
	invokestatic io/putIntLn(I)V
Label10:
	goto Label7
Label6:
Label11:
Label12:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fcmpl
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
Label19:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fadd
	invokestatic io/putFloatLn(F)V
Label20:
	goto Label17
Label16:
Label21:
Label22:
	getstatic MiniGoClass/c F
	getstatic MiniGoClass/d F
	fsub
	invokestatic io/putFloatLn(F)V
Label23:
Label17:
Label13:
Label7:
Label3:
Label1:
	return
.limit stack 6
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
	iconst_5
	putstatic MiniGoClass/a I
	bipush 10
	putstatic MiniGoClass/b I
	ldc 10.0
	putstatic MiniGoClass/c F
	ldc 20.0
	putstatic MiniGoClass/d F
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
