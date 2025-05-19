.source Gadget.java
.class public Gadget
.super java.lang.Object
.field public name Ljava/lang/String;
.field public release_year I

.method public <init>(Ljava/lang/String;I)V
Label0:
.var 0 is this LGadget; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is release_year I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Gadget/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Gadget/release_year I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
Label0:
.var 0 is this LGadget; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public printInfo()V
Label0:
.var 0 is this LGadget; from Label0 to Label1
Label2:
	ldc "Gadget: "
	aload_0
	getfield Gadget/name Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Gadget/release_year I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public changeName(Ljava/lang/String;)V
Label0:
.var 0 is this LGadget; from Label0 to Label1
.var 1 is newName Ljava/lang/String; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Gadget/name Ljava/lang/String;
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
