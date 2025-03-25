// Description: Create a program for St.John's Marina and Yacht Club to create receipts for members
// Author: Kevin Green
// Dates: March 17th, 2025 - March 22nd, 2025

// Define program constants
const EVEN_SITE_RATE = 80.0;
const ODD_SITE_RATE = 120.0;
const ALT_MEM_RATE = 5.0;

const SITE_CLEAN_RATE = 50.0;
const VID_SURV_RATE = 35.0;

const STAND_MEM_RATE = 75.0;
const EXEC_MEM_RATE = 150.0;

const HST_RATE = 0.15;
const CANC_FEE_RATE = 0.6;
const PRO_FEE_RATE = 59.99;

const HST_REG_NO = "549-33-5849-47";

const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});
const per0Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});
const com0Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "0",
  maximumFractionDigits: "0",
});

// Gather user input
let cur_date = prompt("Enter the current date (YYYY-MM-DD): ");
let site_num = prompt("Enter the site number (1-100): ");
site_num = parseInt(site_num);

let mem_name = prompt("Enter the members name: ");
let st_add = prompt("Enter the members street address: ");
let city = prompt("Enter the members city: ");
let prov = prompt("Enter the members province (XX): ").toUpperCase();
let postal = prompt("Enter the members postal code (X#X#X#): ").toUpperCase();
let home_num = prompt("Enter the members home number (##########): ");
let cell_num = prompt("Enter the members cell number (##########): ");

let mem_type = prompt(
  "Enter the members membership type (S / E): "
).toUpperCase();

let alt_mems = prompt("Enter the number of alternate members allowed access: ");
alt_mems = parseInt(alt_mems);

let site_clean = prompt(
  "Enter if member wants weekly site cleaning (Y / N): "
).toUpperCase();

let vid_surv = prompt(
  "Enter if member wants video surveillance (Y / N): "
).toUpperCase();

// Perform required calculations
let site_charges = 0;
if (site_num % 2 === 0) {
  site_charges = EVEN_SITE_RATE + ALT_MEM_RATE * alt_mems;
} else {
  site_charges = ODD_SITE_RATE + ALT_MEM_RATE * alt_mems;
}

let site_clean_charges = 0;
let site_clean_dsp = "";
if (site_clean == "Y") {
  site_clean_charges = SITE_CLEAN_RATE;
  site_clean_dsp = "Yes";
} else {
  site_clean_charges = 0;
  site_clean_dsp = "No";
}

let vid_surv_charges = 0;
let vid_surv_dsp = "";
if (vid_surv == "Y") {
  vid_surv_charges = VID_SURV_RATE;
  vid_surv_dsp = "Yes";
} else {
  vid_surv_charges = 0;
  vid_surv_dsp = "No";
}

let extra_charges = site_clean_charges + vid_surv_charges;
let sub_tot = site_charges + extra_charges;
let hst = sub_tot * HST_RATE;

let tot_montly_charges = sub_tot + hst;

let mem_type_dsp = "";
let monthly_dues = 0;
if (mem_type == "S") {
  monthly_dues = STAND_MEM_RATE;
  mem_type_dsp = "Standard";
} else {
  monthly_dues = EXEC_MEM_RATE;
  mem_type_dsp = "Executive";
}

let monthly_fees = tot_montly_charges + monthly_dues;
let yearly_fees = monthly_fees * 12;
let monthly_pay = (yearly_fees + PRO_FEE_RATE) / 12;
let canc_fee = site_charges * 12 * CANC_FEE_RATE;

// Display results
document.writeln("<br />");

document.writeln("<table class='marinatable'>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2' class='centertext'>St. John's Marina & Yacht Club" +
    "<br />" +
    "Yearly Member Receipt <br /><br /> </td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'> <br /> Client Name and Address: <br /><br /> </td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>" +
    mem_name +
    "<br />" +
    st_add +
    "<br />" +
    city +
    ", " +
    prov +
    ", " +
    postal +
    "<br /><br />" +
    "Phone: " +
    home_num +
    " (H)" +
    "<br />" +
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
    cell_num +
    " (C)</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'> Site #: " +
    site_num +
    "<span class='righttext'>" +
    "Member type: " +
    mem_type_dsp +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.write(
  "<td colspan='2'>Alternate members: " +
    "<span class='righttext'>" +
    alt_mems +
    "</span>" +
    "<br /> Weekly site cleaning: " +
    "<span class='righttext'>" +
    site_clean_dsp +
    "</span>" +
    "<br > Video surveillance: " +
    "<span class='righttext'>" +
    vid_surv_dsp +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Site charges: " +
    "<span class='righttext'>" +
    cur2Format.format(site_charges) +
    "</span>" +
    "<br /> Extra charges: " +
    "<span class='righttext'>" +
    cur2Format.format(extra_charges) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Subtotal: " +
    "<span class='righttext'>" +
    cur2Format.format(sub_tot) +
    "</span>" +
    "<br /> Sales tax (HST): " +
    "<span class='righttext'>" +
    cur2Format.format(hst) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Total monthly charges: " +
    "<span class='righttext'>" +
    cur2Format.format(tot_montly_charges) +
    "</span>" +
    "<br /> Monthly dues: " +
    "<span class='righttext'>" +
    cur2Format.format(monthly_dues) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Total monthly fees: " +
    "<span class='righttext'>" +
    cur2Format.format(monthly_fees) +
    "</span>" +
    "<br /> Total yearly fees: " +
    "<span class='righttext'>" +
    cur2Format.format(yearly_fees) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Monthly payment: " +
    "<span class='righttext'>" +
    cur2Format.format(monthly_pay) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln(
  "<td colspan='2'>Issued: " +
    "<span class='righttext'>" +
    cur_date +
    "</span>" +
    "<br /><br /> HST Reg No: " +
    "<span class='righttext'>" +
    HST_REG_NO +
    "</span>" +
    "<br /><br /> Cancellation Fee:" +
    "<span class='righttext'>" +
    cur2Format.format(canc_fee) +
    "</span>" +
    "</td>"
);
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='blackbar'></td>");
document.writeln("</tr>");
document.writeln("</table>");
