.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LGoString;
.field static c LGoString;
.field static d LGoString;
.field static e LGoString;
.field static f LGoString;
.field static g LGoString;
.field static h LGoString;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/c LGoString;
	invokevirtual GoString/compare(LGoString;)I
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/d LGoString;
	invokevirtual GoString/compare(LGoString;)I
	ifge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
Label15:
Label16:
	getstatic MiniGoClass/a LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label17:
	goto Label14
Label13:
Label18:
Label19:
	getstatic MiniGoClass/c LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label20:
Label14:
Label10:
	goto Label7
Label6:
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/d LGoString;
	invokevirtual GoString/compare(LGoString;)I
	ifge Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
Label25:
Label26:
	getstatic MiniGoClass/d LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label27:
	goto Label24
Label23:
Label28:
Label29:
	getstatic MiniGoClass/e LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label30:
Label24:
Label7:
	getstatic MiniGoClass/a LGoString;
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/compare(LGoString;)I
	ifne Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label33
Label35:
Label36:
	getstatic MiniGoClass/f LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label37:
	goto Label34
Label33:
Label38:
Label39:
	getstatic MiniGoClass/g LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label40:
Label34:
Label3:
Label1:
	return
.limit stack 13
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label41:
Label42:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LGoString;
	new GoString
	dup
	ldc "xin chao"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/c LGoString;
	new GoString
	dup
	ldc "Bonjour"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/d LGoString;
	new GoString
	dup
	ldc "Hallo"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/e LGoString;
	new GoString
	dup
	ldc "Ciao"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/f LGoString;
	new GoString
	dup
	ldc "Konnichiwa"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/g LGoString;
	new GoString
	dup
	ldc "Annyeonghaseyo"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/h LGoString;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
