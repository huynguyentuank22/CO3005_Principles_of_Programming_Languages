.source Owner.java
.class public Owner
.super java.lang.Object
.field public owner_name Ljava/lang/String;
.field public gadget_count I
.field public avg_rating F
.field public main_gadget LGadget;

.method public <init>(Ljava/lang/String;IFLGadget;)V
Label0:
.var 0 is this LOwner; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is owner_name Ljava/lang/String; from Label0 to Label1
.var 2 is gadget_count I from Label0 to Label1
.var 3 is avg_rating F from Label0 to Label1
.var 4 is main_gadget LGadget; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Owner/owner_name Ljava/lang/String;
	aload_0
	iload_2
	putfield Owner/gadget_count I
	aload_0
	fload_3
	putfield Owner/avg_rating F
	aload_0
	aload 4
	putfield Owner/main_gadget LGadget;
Label3:
Label1:
	return
.limit stack 6
.limit locals 5
.end method

.method public <init>()V
Label0:
.var 0 is this LOwner; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public displayProfile()V
Label0:
.var 0 is this LOwner; from Label0 to Label1
Label2:
	ldc "Owner: "
	aload_0
	getfield Owner/owner_name Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Owner/gadget_count I
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Owner/avg_rating F
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield Owner/main_gadget LGadget;
	invokevirtual Gadget/printInfo()V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
