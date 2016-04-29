#! C:/Dwimperl/perl/bin/perl.exe
use lib "$ENV{DOCUMENT_ROOT}/cgi/modules";
use CGI;
use strict;
use Data::Dumper;
use Database;

my $q = new CGI;
print $q->header('text/html');

my $action = $q->param('action') || '';

if ($action eq 'add') {
	add_product ();
} elsif ($action eq 'delete') {

}
else {
	show_add_product_html();
}

sub show_add_product_html {
	print qq~
	<html lang="en">
	<head>
	<link rel="stylesheet" href="/html/Skeleton-2.0.4/css/skeleton.css">
	<link rel="stylesheet" href="/html/Skeleton-2.0.4/css/normalize.css">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	.cb {clear: both;}
	.error { font-size: 12px; color: red;}
	.mt5 { margin-top: 5px;}
	.mt20 { margin-top: 20px;}
	.dfx { display: flex;}
	</style>
	</head>

	<body>
	<div id="main" style="width: 50%; margin-left: 25%; margin-top: 2%;">
		<div class="u-full-width" style="margin-top: 3%; margin-bottom: 3%; text-align: center; font-size: 29px; font-weight: bold;"> Add New product </div>
		<form class="u-full-width" action="" method="post">
			<div class="six columns">
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Product Name :</div><input type="text" style="width: 250px; height: 27px;" placeholder="Product Name" name="prd_name"> <span style="margin-left: 5px; color: red;">*</span> </div>
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Category :</div>
				<select class="u-full-width" id="prd_type" name="prd_type">
					<option value="1">Select</option>
					<option value="2">Footwear</option>
					<option value="3">Apparel</option>
					<option value="4">Bags and Luggage</option>
					<option value="5">Electronics</option>
					<option value="6">Beauty</option>
				</select></div>
				 <textarea class="u-full-width mt5" name="prd_desc" placeholder="Product description" style="resize: none; height: 170px;"></textarea>
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Quantity per unit :</div><input type="text" name="prd_qty" style="width: 250px; height: 27px;" placeholder="Quantity per unit"></div>
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Unit Price :</div><input type="text" name="prd_price" style="width: 250px; height: 27px;" placeholder="Unit price"> <span style="margin-left: 5px;">INR</span> </div>
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Unit Weight :</div><input type="text" style="width: 250px; height: 27px;" placeholder="Unit Weight" name="prd_wt"> <span style="margin-left: 5px;">gm</span> </div>
				<div class="u-full-width mt5 dfx"> <div style="width:150px">Unit In stock :</div><input type="text" style="width: 250px; height: 27px;" placeholder="Unit In stock" name="prd_stock"> </div>
				 <textarea class="u-full-width mt5" placeholder="Product note" style="resize: none; height: 170px;" name="prd_note"></textarea>
				 
				 <div style="text-align: center;" class="mt20">
		  <input class="button-primary" type="submit" value="Submit">
		  <input class="button-primary" type="button" value="Clear">
		  </div>
		  </div>
		  <input type = "hidden" name="action" value="add"/>
		</form>
	</div>
	</body>
	</html>
	~;
}

sub add_product {
	my $prd_name  = $q->param('prd_name') || '';
	my $prd_type  = $q->param('prd_type') || '';
	my $prd_qty   = $q->param('prd_qty') || '';
	my $prd_price = $q->param('prd_price') || '';
	my $prd_desc  = $q->param('prd_desc') || '';
	my $prd_wt    = $q->param('prd_wt') || '';
	my $prd_stock = $q->param('prd_stock') || '';
	my $prd_note  = $q->param('prd_note') || '';
		
	my $query = qq~insert into products (ProductName, ProductDescription, CategoryID, QuantityPerUnit, UnitPrice, UnitWeight, UnitsInStock, Note )
		values ('$prd_name' ,'$prd_type' ,'$prd_qty'  ,'$prd_price' ,'$prd_desc' ,'$prd_wt'   ,'$prd_stock' ,'$prd_note' )		~;
	# my $row = Database::exec_query({query=>$query});
	
	my $dbh = Database::getDbh();
	my $sth = $dbh->prepare("insert into products (ProductName, ProductDescription, CategoryID, QuantityPerUnit, UnitPrice, UnitWeight, UnitsInStock, Note ) values (?,?,?,?,?,?,?,?)");
	$sth->execute($prd_name ,$prd_desc ,$prd_type,  $prd_qty,$prd_price , $prd_wt   ,$prd_stock ,$prd_note);
	print "insertd rows" if $sth->rows;
}