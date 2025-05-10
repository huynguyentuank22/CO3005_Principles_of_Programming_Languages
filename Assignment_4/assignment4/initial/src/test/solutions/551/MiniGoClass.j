.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LString_MiniGo;
.field static c LString_MiniGo;
.field static d LString_MiniGo;
.field static e LString_MiniGo;
.field static f LString_MiniGo;
.field static g LString_MiniGo;
.field static h LString_MiniGo;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a LString_MiniGo;
	getstatic MiniGoClass/c LString_MiniGo;
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
Label9:
	getstatic MiniGoClass/a LString_MiniGo;
	getstatic MiniGoClass/d LString_MiniGo;
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	ifge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
Label15:
Label16:
	getstatic MiniGoClass/a LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label17:
	goto Label14
Label13:
Label18:
Label19:
	getstatic MiniGoClass/c LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label20:
Label14:
Label10:
	goto Label7
Label6:
	getstatic MiniGoClass/a LString_MiniGo;
	getstatic MiniGoClass/d LString_MiniGo;
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	ifge Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
Label25:
Label26:
	getstatic MiniGoClass/d LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label27:
	goto Label24
Label23:
Label28:
Label29:
	getstatic MiniGoClass/e LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label30:
Label24:
Label7:
	getstatic MiniGoClass/a LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/compare(LString_MiniGo;)I
	ifne Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label33
Label35:
Label36:
	getstatic MiniGoClass/f LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label37:
	goto Label34
Label33:
Label38:
Label39:
	getstatic MiniGoClass/g LString_MiniGo;
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
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
	new String_MiniGo
	dup
	ldc "Hello"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LString_MiniGo;
	new String_MiniGo
	dup
	ldc "xin chao"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/c LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Bonjour"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/d LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Hallo"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/e LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Ciao"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/f LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Konnichiwa"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/g LString_MiniGo;
	new String_MiniGo
	dup
	ldc "Annyeonghaseyo"
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/h LString_MiniGo;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
