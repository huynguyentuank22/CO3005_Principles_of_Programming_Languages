.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a Z
.field static b Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a Z
	invokestatic io/putBoolLn(Z)V
	getstatic MiniGoClass/b Z
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 1
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
	iconst_5
	bipush 7
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putstatic MiniGoClass/a Z
	ldc 5.0
	ldc 7.0
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	putstatic MiniGoClass/b Z
Label0:
Label1:
	return
.limit stack 7
.limit locals 0
.end method
