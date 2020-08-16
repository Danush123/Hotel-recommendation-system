<%@ page import="javax.util.*" %>
<%@ page import="java.util.*" %>
<%@ page import="javax.sql.*" %>
<%@ page import="java.sql.*" %>
<%
String s1=request.getParameter("email");
String s2=request.getParameter("pass");
try{
Class.forName("com.mysql.jdbc.Driver");
Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/cip","root","");
Statement st=conn.createStatement();
//String queryString = "SELECT name,pass FROM signup where user='"+s1+"' and pass='"+s2+"'";
//ResultSet results = st.executeQuery(queryString);
//if(!results.next()) {
  //          out.println("Wrong Username and Password.");
  //      }
//else
//{
//  out.println("Validated.");
//}
/*boolean flag = false;

        String queryString = "select user,pass from signup";
        ResultSet results = st.executeQuery(queryString);

        while (results.next()) {
        String name = results.getString("user");
        String password =  results.getString("pass");

           if ((s1.equals(name)) && (s2.equals(password))) {
              flag = true;
               out.println("Username and Password exist");
        }
        results.close();
        if(!flag){
               out.println("Please Check Username and Password ");
        }
    }
*/
ResultSet rs=st.executeQuery("select * from signup where user='"+s1+"' and pass='"+s2+"'");
           int count=0;
           while(rs.next()){
           count++;
          }
          if(count>0){
           out.println("welcome "+s1);
		   response.sendRedirect("http://localhost:8080/booking/booking.html");
           }
          else{
           response.sendRedirect("http://localhost:8080/Login/index.html");
          }
}

catch(Exception e)
{
  System.out.print(e);
  e.printStackTrace();
}


%>
