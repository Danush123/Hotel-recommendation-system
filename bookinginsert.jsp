<%@ page import="javax.util.*" %>
<%@ page import="java.util.*" %>
<%@ page import="javax.sql.*" %>
<%@ page import="java.sql.*" %>
<%
//  PrintWriter out=response.getWriter();
  String s1=request.getParameter("first_name");
  String s2=request.getParameter("phone");
  String s3=request.getParameter("hotel");

  try{
  Class.forName("com.mysql.jdbc.Driver");
  Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/cip","root","");
  Statement st=conn.createStatement();
  st.execute("insert into booking values('"+s1+"','"+s2+"','"+s3+"')");
  }
  catch(Exception e)
  {
    System.out.print(e);
    e.printStackTrace();
  }
  out.println("Inserted.....");
  response.sendRedirect("http://localhost:8080/Credit Card Payment/payment.html");
%>
