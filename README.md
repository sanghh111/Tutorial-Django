<b>
Lộ trình học DJango của mình:

<li>Đầu tiên mình sẽ đọc hết tài liệu và thực hành hết ở trên trang turrial và mình sẽ tổng kết lại sau<br>
<li>Tìm hiều về API DATABASE mình thấy khá hay nên cần tìm hiểu kĩ về nó.
<li> Mình sẽ lên bài test sau khi hoàn thành turrial trên trang document của django
<li>Sau đó mình nghĩ học tiếp rest api của django
<li>Tập làm quen framework flask

<br>
<br>

</b>



<center>
 <h1>  Django 01: Viết ứng dụng django đầu tiên phần 1  </h1> 
</center>




Bài viết này mình dựa trên nghiên cứu trên: https://docs.djangoproject.com/en/4.0/intro/tutorial01/


Tổng quan bài viết:
<li><a><b>Khởi tạo dự án</b></a></li>
<li><a><b>Phát triển máy chủ</b></a></li>
<li><a><b>Tạo ứng dụng bình chọn</b></a></li>
<li><a><b>Lần đầu tiên viết views</b></a></li>

Trong bài lần này chúng ta sẽ tạo ra 1 ứng dụng bình chọn:

<li> Một trang để cho người dùng bình chọn </li>
<li> Một trang admin bạn có thể thêm, xóa /, sửa các câu bình chọn</li>


<h2>1. Khởi tạo dự án </h2>

<br> 

Đây là một bước bắt đầu dự án của bạn. Cụ thể là, bạn cần phải gõ vài câu lệnh để nó xây dựng project- là tập hợp bộ cài đặt cho dự án django của bạn, bao gồm cấu hình cơ sở dữ liệu, các tùy chỉnh riêng dành cho Django và cài đặt dành riêng cho ứng dụng.

Ở trong command-line hãy cd tới thu mục mà ban muốn tạo dự án và gõ lệnh này 

<center>

   <code> <b> django-admin startproject "tên project" </b></code>

</center>

<br>

Nó sẽ tạo lên một project ngay tại nơi bạn đang trỏ tới.


<table>
    <b><th>Lưu ý</th></b>
        <td> Bạn cần phải tránh đặt trùng với các thành phần của python và django được tích hợp sẵn. Cụ thể là tên cần tránh như là <b>django</b>( nó sẽ ảnh hưởng với django của bạn) hoặc là <b>test</b>( nó ảnh hưởng tới các thư viện có sẵn của Pyhton) </td>
</table>
    
<table>
    <b><tr>Chúng ta nên viết code ở đâu</tr></b>
    <td>Với PHP thường đặt code thư mục root ở web server (var/www). Còn với Django sẽ không làm như vậy. Nó không phải là một ý tưởng hay đẻ đặt bất kì dòng code python nào dưới thư mục root ở web server bởi vì có nguy cơ dẫn đến khả năng người khác có thể xem được code của web của bạn.<br> <br>
    Đặt code của bạn ở đường dẫn <b>outside</b> ở tài liệu gốc, như là <b>/home/mycode/</b></td>
<table>

Chúng ta hãy xem project đã tạo:

<table>
<td>
    Tên project/<br>    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;manage.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tênProject.py/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__init__.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setting.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;urls.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;asgi.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wsgi.py
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</td>
</table>

Các file là:

<li>file có <b>tên project</b> là đường dãn gốc là nơi nó chứa tất cả dự án của bạn. Tên của file không quan trọng bạn có thể bất cứ cái gì bạn thích.</li>

<li><b>manage.py</b> là một dòng lệnh tiện ích mà bạn có thể tương tác với dự án django bằng nhiều cách khác nhau. Bạn có thể đọc chi tiết về manage.py tại <a href = "https://docs.djangoproject.com/en/4.0/ref/django-admin/"><u>django-admin and manage.py.</u></a></li>

<li>Vào bên trong đường dẫn <b>mysite/</b> là các gói quan trọng cho dự án của bạn. Tên của nó là một thư viện python được gọi bất kì thứ gì ở bên trong (ví dụ <b>tênProjec.urls</b>) </li>

<li><b>tênProject/__init__.py</b> là một file trống python được cho  biết rằng thư mục này được coi là một thư viện của python </li>

<li><b>tênProject/setting.py</b> Cài đặt cấu hình hình cho dự án về django.<a href = "https://docs.djangoproject.com/en/4.0/topics/settings/"><u>Django setting</u></a> sẽ cho bạn biết làm cách nào bạn cấu hình.</li>

<li><b>tênProject/urls.py</b>: đường dẫn url cho dự án django của bạn, mục lục của trang django. Bạn có thể đọc nhiều hơn ở <a href =https://docs.djangoproject.com/en/4.0/topics/http/urls/"><u>URL dispatcher.</u></a><li>

<li> <b>tênProject/asgi.py</b> một điểm vảo tương thích ASGI web server để bảo mật project của bạn. Xem <a href = "https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/"><u>làm thế nào để hoạt động</u></a>để biết thêm chi tiết </li>

<li> <b>tênProject/wsgi.py</b> một điểm vảo tương thích WSGI web server để bảo mật project của bạn. Xem <a href = "https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/"><u>làm thế nào để hoạt động</u></a>để biết thêm chi tiết </li>

<br>
<h2>Phát triển máy chủ</h2>

Hãy chắc chắn rằng dự án Django của bạn hoạt động. Chắc chắn rằng ở terminal của bạn đang focus tới thư mục dự án của mình:


<center> <code> python manage.py runserver </code> </center>

Bạn sẽ thấy dòng lệnh như sau:<br><br>
<code>
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

February 16, 2022 - 15:50:53
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
    </code>


Bạn đã bắt đầu phát triển máy chủ django, một máy chủ được viết hoàn toàn bằng python. Với tính năng này bạn có thể phá triển nhanh chóng mà không cần cấu hình máy chủ - như là apache - cho đến khi bạn dã chuẩn bị quá trình triển khai.

<h2>Tạo ứng dụng bình chọn</h2>

Bây giờ môi trường dự án của bạn đã được thiết lập, bắt tay vào làm dự án nào.

Mỗi ứng dụng viết bằng django bao gồm một gói Python tuân thủ theo một quy ước nhất định. Django đi kèm với một tiện ích tự động tạo cấu trúc thư mục cơ bản của ứng dụng, vì vậy bạn có thể tập trung vào việc viết mã hơn là tạo thư mục.

<Table>
    <th>
    App vs Project
    </th>
    <td>
    Điểm khác biệt giữa app và project là gì? App là một ứng dụng web mà nó có thể thực hiện điều gì đó như là một trang blog,  một trang có thể cho mọi người bỏ phiếu với dữ liệu có trong cơ sở dữ liệu. Một project là bộ cấu hình và ứng dụng. Một dự án có thể chứa nhiều app. Một app có thể có nhiều dự án
    </td>
</Table>

Ở trong bài học lần này, chúng ta sẽ tạo một ứng dụng điền từ mình tạo cùng đường dẫn với file <b>manage.py</b>.


Để tạo app, bạn phải chắc chắn rằng bạn đang ở cùng thư mục với file <b>manage.py</b> và câu lệnh như sau:

<code> python manage.py startapp polls </code>

<b>
Note:
    Để tương tác được với django chúng ta gọi file <b>manage.py</b> để bắt đầu dự án chúng ta dùng câu lệnh startappp và polls la tên mình đặt các bạn có thể đặt sao cũng được.
</b>
<br>
<br>
Nó sẽ tạo ra thư mục theo tên_app:
<!-- <code> -->
<table>
    <tr>
polls/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    __init__.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    admin.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    apps.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    migrations/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        __init__.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    models.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    tests.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    views.py<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</tr>
</table>
<!-- <code> -->


Và đây là cấu trúc của ứng dụng của mình.


<h2> Lần đầu viết View </h2>

Bắt đầu vào viết view. vào view ở trong thư mục app chúng ta mới tạo và chúng ta hãy viết theo dòng code như sau:

<table>
<th>
polls/views
</th>
<td>
<code>from django.http import HttpResponse<br>
def index(request):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return HttpResponse("Hello my name is Sang")
<code>
</td>
</table>

Câu hỏi số 1:
<li> Httprespone gọi ra gì?
<li> request trong index làm gì? Không thêm nó có chạy hay không
<br>
<br>
Đây là view đơn giản nhất trong django. Để gọi tới view, chúng ta cần map nó tới URL - và để làm được điều đố chúng ta phải cấu hình.

Để hiểu polls hiểu được view chúng ta mới tạo thì chúng ta tạo file <b>urls.py</b>

<br>
<p>Hãy thêm code vào  trong file urls.py của chúng ta mới tạo:<p>


<table>
    <th>polls/urls.py</th>
    <td><b>from django.urls import path<br>from . import views

    urlpatterns = [
    path('', views.index, name='index'),]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</b></td>
</table>

Bước tiếp theo, vào urls của project để chúng ta cấu hình url của app. Chúng ta gọi tới thư viện django.urls.include và thêm một hàm include ở trong danh sách urlpartern, bạn sẽ có:

<table>
    <th>myProject/urls.py</th>
    <td><code>
from django.contrib import admin<br>
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/',include('polls.urls')),
]

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</code></td>
</table>

Hàm include cho phép tham chiếu tới các url đã cấu hình, khi django gọi tới include(), nó cắt bỏ bất kỳ phần nào của URL khớp với thời điểm đó và gửi chuỗi còn lại đến URLconf được bao gồm để xử lý thêm.

ý tưởng ẩn sau trong hàm include() là làm cho URL <b> plug-and-play </b>trở nên dễ dàng. 

<table>
    <th> Khi nào sử dụng hàm include()
    </th>
    <td> Bạn nên sử dụng hàm include() ở mọi nơi ngoại trừ mẫu url admin.site.urls
    </td>
</table>

Bạn đã viết xong trong indexx bây giờ chúng ta cho chúng chúng chạy:

<center><code> python manage.py  runserver </code></center>

Go to http://localhost:8000/polls trong trong trình duyệt bạn sẽ thấy "Hello my name is Sang"

Hàm path() được thông qua bởi 4 tham số, 2 tham só bắt buộc : <b> route </b> và <b> view </b> và 2 không bắt buộc : <b> kwargs </b> và <b>name</b>. Chi tiết về 4 tham số:


<h3>Tham số route</h3>

Route là một chuỗi chứa các mẫu url. khi có một yêu cầu thực hiện, django sẽ bắt đầu từ mẫu đàu tiên ở trong danh sách mẫu url và duyệt tuần tụ, và so sánh với url được yêu cầu cho đén khi tìm được.

Mẫu không thể tìm kiếm các thông số GET và POST. Ví dụ, ở một request đến <b>https://www.example.com/myapp/</b> cấu hình url sẽ tìm kiếm <b>myapp/</b>. Ở trong request <b>o https://www.example.com/myapp/?page=3</b> cấu hình url cũng chỉ tìm tới <b>myapp/</b>.

<h3> Tham số view </h3>

Khi djaango dẫ tìm đúng mẫu url nó sẽ chỉ định tới hàm view với đối tượng Httrequest với đối số đầu tiên (theo ý mình đối số đầu tiên là request.)


<h3> Tham số kwargs </h3>

Bất kì tham só có thể thông qua kiểu dictionary để đến view. Trong tương lai tôi sẽ không sử dụng cái này trong phần mở đầu này.

<h3> Tham số name </h3>

Cái việc đặt tên cho url của bạn để cho bạn dễ dàng tìm kiếm nó ở bất cứ nơi nào trong django, đặt biệt là trong các mẫu. Điều đặc biệt của tính năng này cho phép bạn thực hiện thay đổi cục bộ các mẫu url trong dự án của bạn khi bạn muốn mở cái file đó lên.


<b> Ở bài học số 1 bạn hãy chắc chắn rằng các bạn phải hiểu thật kĩ về request và phản hồi từ chương trình. Ở bài học thứ 2 chúng ta sẽ làm quen với databasedatabase. </b>







<br>
<br>
<br>
<br>
<br>

<h1>Bại học số 2  </h1>



Ở bài học này bạn sẽ thiết lập database, tạo model đầu tiên và giới thiệu nhanh django tự động tạo một trang admin. 

<h2> Thiết lập database </h2>

Bây giờ, mở file <b> mysite/setting.py </b>. Nó là một module bình thường của python với các biến cấp module đại diện cho cài đặt django.<br><br>


Theoo mặc định, cấu hình sử dụng là SQLite. Nếu như bạn chưa quen với database hoặc bản chỉ quan tâm thì django, thì sqlite là là chọn tốt nhất nó ở trong Python, vì vậy bạn ko cần cài đặt bất kì thứ gì khác để hộ trợ cơ sở dữ liệu cảu bạn. Khi bạn bắt đầu vào một dự án thực sự, tuy nhiên bạn có thể mở rộng database như là PostgreSQL, để trách đau đầu khi chuyển database.<br><br>

Nếu bạn muốn sử dụng cơ sở dữ liệu khác, hãy tải các <a href = "https://docs.djangoproject.com/en/4.0/topics/install/#database-installation" >database</a> thích hợp và thay đổi từ khóa trong danh mục <b> DATABASE 'default' </b> để khớp với các cấu hình kết nối database:

<li> <a href = "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASE-ENGINE">ENGINE</a>: <b>'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'</b>. Một số backend khác <a href = "https://docs.djangoproject.com/en/4.0/ref/databases/#third-party-notes">có sẵn</a></li>

<li><a href = "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-NAME">Name</a>: Cái tên của cơ sở dữ liệu của bạn. Nếu bạn dùng SQLite, cơ sở dữ liệu của bạn nó sẽ là một file trên máy tính cảu bạn. Trong trường hợp, NAME là một đường dẫn tuyệt đói, bao gồm tên file. Giá trị mặc định, <b>BASE_DIR /  'db.sqlite3'</b> sẽ được lưu trữ trên thư mục project của bạn.</li>

Nếu bạn không sử dụng sqlite là cơ sở dữ liệu, thêm cấu hình như là <b>USER, PASSWORK, HOST </b> phải được thêm. Mọi chi tiết, xem tài liệu tham khảo <a href = "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASES"> cơ sở dữ liệu </a>.

Khi bạn muốn thiết kế <b> mysite/setting.py</b>. Đặt <a href= "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-TIME_ZONE">TIME_ZONE</a> ở nơi của bạn. 

Cũng vậy, lưu ý cấu hình <a href = "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-INSTALLED_APPS">INSTALL_APPS</a> ở đàu tệp. Nó giữ các tên của tất cả các ứng dụng django mà nó đã được đã kích hoạt trong phiên bản django. Ứng dụng có thể sử dụng trong nhiều projects, và bạn có thể gói và phân phát cho nhiều project. 

Theo mặc định, <a href = "https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-INSTALLED_APPS">INSTALL_APPS</a> chứa các ứng dụng sau đây, tất cả đi kèm với django:
<li><a href = "https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#module-django.contrib.admin">django.contrib.admin </a>: trang admin, bạn sẽ sử dụng trong thời gian ngắn.
<li><a href= "https://docs.djangoproject.com/en/4.0/topics/auth/#module-django.contrib.auth" >django.conrtrib.auth</a>: Hệ thống xác thực.
<li> <a href= "https://docs.djangoproject.com/en/4.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes">django.contrib.contenttypes </a>:
<li><a href= "https://docs.djangoproject.com/en/4.0/topics/http/sessions/#module-django.contrib.sessions">django.contrib.sessions </a>: 
<li> <a href= "https://docs.djangoproject.com/en/4.0/ref/contrib/messages/#module-django.contrib.messages">django.contrib.messages  </a>:
<li> <a href = "https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles">django.contrib.staticfiles </a>:

Mình sẽ câp nhập sau.


Các ứng dụng đã được giới thiệu ở trên theo mặc định như một sự thuận tiện cho trường hợp thông thường.

Trong số các ứng dụng trên sử dụng ít nhất một bảng cơ sở dữ liệu, tuy nhiên, vì vậy chúng ta cần tạo các bảng cơ sở dữ liệu trước khi có thêr sử dụng chúng. Để làm đièu này chúng ta sử dụng lệnh sau:

<center> <code>  python manage.py migrate </code> </center>


Dòng lệnh <b>migrate</b> được nhìn vào cấu hình INSTALLED_APPS và các bản cở sở dữ liệu cần thiét được dựa theo câu hình trong file <b>mysite/setting.py</b> và các di chuyển cở sở dữ liệu được vận chuyển cùng với ứng dụng. 


<h2> Tạo mô hình </h2>


Bây giờ chúng ta định nghĩa bản chất các mô hình, với siêu dữ liệu bổ sung.

Chúng ta quay lại ứng dụng bỏ phiếu của chúng ta, chúng ta sẽ 2 mô hình gồm: <b>Question</b> và <b>Choice</b>. Mô hình Question gồm có các thuộc tính như là tên câu hỏi và ngày xuất bản và mô hình Choice tên câu trả lời và số lượt bỏ phiếu. Với mới câu trả lời sẽ liên kết tới vơi một câu hỏi.

Các khái niệm được đại diện bằng Python class. Chỉnh sửa polls/models.py   sẽ trông như thế này:
<br>--------------------------------------------------------------------------------------------------<b><br>polls/models.py</b><br>--------------------------------------------------------------------------------------------------<br>
<code>from django.db import models<br><br>class Question(models.Model):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;question_text = models.CharField(max_length=200)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pub_date = models.DateTimeField('date published')
<br><br>
class Choice(models.Model):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;question = models.ForeignKey(Question, on_delete=models.CASCADE)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;choice_text = models.CharField(max_length=200)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;votes = models.IntegerField(default=0)</code>
<br>--------------------------------------------------------------------------------------------------<br>

Bây, mỗi mô hình được đại diện cho một lớp con <b>django.db.models.Model</b> Một mô hình có nhiều biến lớp, một trong số đó đại điện cho truòng dữ liệu trong mô hình.<br><br>

Mỗi một thuộc tính đại diễn cho một phiên bản class Field - ví dụ: CharField cho kiểu chuỗi và DateTimeField cho thơi gian. Điêu này nói lên Django biết kiểu dữ liệu mỗi trường nằm giữu.<br><br>

Tên của mỗi cá thể trong trường (như là question_text, pub_date) là tên của trường đó, ở định dạng thân thiện của máy. Bạn có thể sử dụng giá trị ở trong code python, và ở cở sở dữ liệu của bạn sẽ sử dụng với tên của cột.<br><br>


Bạn có thể sử dụng một đối số đàu tiên tùy chọn ở trong Field để chỉ định 
một tên cho người đọc. Nếu bạn không cung cấp Django sẽ sử dụng tên máy có thể đọc được.<br><br>


Một vài trường, có yêu cầu tham só. Ví dụ CharField có tham số max_length.Điều đó không chỉ được sử dụng trong lược đồ cơ sở dữ liệu mà còn được sử dụng trong quá trình xác thực, như chúng ta sẽ sớm thấy.<br><br>

Một Field có thể cũng nhiều tham số tùy chọn. Ví dụ lượt votes của Choice chúng ta đặt default bằng 0.<br><br>

Cuối cùng, chú ý một một quan hệ được định nghĩa, sử dụng khóa phụ Forrginkey.  ĐIều này có nghĩa mỗi choice có một liên hệ tới duy nhất 1 Question. Django có hỗ trọ về quan hệ many to many, many to one, one to one.

<h2> Kích hoạt mô hình</h2>


Một chút ít của code mô hình cho django khá nhiều thông tin. Với Django, có khả năng để:
<li>Tạo bảng dữ liệu cho ứng dụng
<li>Tạo 1 API truy cập database cho việc truy cập đến đối tượng Question và Choice 

Nhưng đầu tiên chúng ta nói cái project chúng ta ứng dụng polls được cài đặt.

Bao gồm ứng dụng trong project, chúng tôi cần thêm một tham chiếu đến cấu hình của nó trong câu hình INSTALL_APPS. Lớp PollsConfig ở trong <b>polls/apps.py</b> vì vậy tên nó là <b>'polls.apps.PollConfig'</b>. Sửa chũa lại settings.py trong thư mục mysite add tên gọi nãy vào trong cấu hình INSTALL_APPS.


<br>--------------------------------------------------------------------------------------------------<b><br>mysite/settings.py</b><br>--------------------------------------------------------------------------------------------------<br>
INSTALLED_APPS = [
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'polls.apps.PollsConfig',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.admin',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.auth',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.contenttypes',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.sessions',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.messages',
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    'django.contrib.staticfiles',
]
<br>--------------------------------------------------------------------------------------------------<br>

Bây giờ Django đã biết bao gồm polls app. Bây giờ t gõ lệnh:

<center><code>python manage.py makemigrations polls</code></center>

Bạn sẽ thấy dòng lệnh tương tự như vậy:

<br>--------------------------------------------------------------------------------------------------<b><br>mysite/settings.py</b><br>--------------------------------------------------------------------------------------------------<br>

Migrations for 'polls':
&nbsp;&nbsp;  polls/migrations/0001_initial.py
&nbsp;&nbsp;&nbsp;&nbsp;    - Create model Question
&nbsp;&nbsp;&nbsp;&nbsp;    - Create model Choice

<br>--------------------------------------------------------------------------------------------------<br>

Bằng cách chạy <b>makemigrations</b>, bạn đang nói với django rằng bạn đã thực hiện một số thay đổi với mô hình và điều đố bạn muốn sự thay đổi được lưu trự tại migration. <br> <br>

Migration là cách django lưu trữ sự thay đổi cho mô hình của bạn- Bạn có thể đọc migaration cho mô hình mới của bạn nếu bạn thích. Bạn đừng lo lắng, bạn không mong đợi để đọc khi nó tạo ra 1 file nhưng chúng được thiết kế để con người có thể chỉnh sửa trong trường hợp bạn muốn chỉnh sửa thủ công cách Django thay đổi mọi thứ. <br> <br>

Câu lệnh trên sẽ chạy migration cho bạn và quản lý tự động các bản cơ sở dữ liệu -  nó được gọi là migrate- chúng ta sẽ nhìn xem sql mà migrate sẽ chạy cái gì. Câu lệnh sqlmigrate có nhận tên của migrate và nó sẽ trả về SQL:

<center><code>python manage.py sqlmigrate polls 0001</code></center>

Bạn sẽ thấy câu lệnh như sau:
<br>--------------------------------------------------------------------------------------------------<br>
<!-- <code> -->
BEGIN;

-- Create model Question
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
<!-- -- -->
-- Create model Choice
<!-- -- -->
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
</code>
<br>--------------------------------------------------------------------------------------------------<br>


Lưu ý những điều dưới đây:

<li> Đầu ra chính xác sẽ là thay đổi tùy thuộc vào cơ sở dữ liệu mà bạn sử dụng. Ví dụ trên tạo cho PostgreSQL.

<li> Tên cuả bảng được tạo ra một cách tự động bằng cách kết hợp tên của ứng dụng(polls) và chuyển thành chữ thường với tên của mô hình -<b>question</b> và <b>choice</b>.
<li>Khóa chính(IDs) sẽ được thêm một cách tự động. (Bạn có thể gọi đè điều này)
<li>Theo quy ước, Django sẽ thêm "_id" cho tên trường khi dùng khóa ngoại. 
<li>Quan hệ của khóa ngoại được tạo ra rõ ràng bởi ràng buộc khóa ngoại. Dừng lo về phần có thể xác định; nó đang nói PostgreSQL không thi hành khóa ngoại cho đến khi kết thúc một tran. 
<li>Nó phù hợp cho cơ sở dữ liệu bạn đang sử dụng, vì vậy trường hợp dành riêng cho cở sở dữ liệu như là <b>auto_increment</b>(MYSQL),<b>serial</b>(PostgreSQL) hoặc <b>interger primary key autoincrement</b>(SQLite) được thực thi cho bạn một cách tự động. Tương tự đối với trích dẫn tên trường - ví dụ: sử dụng dấu ngoặc kép hoặc dấu nháy đơn.
<li>Câu lệnh sqlmigrate  không thật sự chạy migratioon trên cở sử dữ liệu của bạn- thay vì đó, nó in ra màn hình để bạn có thể thấy những gì Django yêu cầu. Nó có ích cho việc kiểm tra Django đang làm cái gì hoặc nếu bạn người quản trị cơ sở dữ liệu mà bạn yêu một đoạn thay đổi cảu SQL.

Nếu bạn quan tâm, bạn cũng có thể chạy <b>python manage  check</b> kiểm tra này cho tất cả lỗi của project của bạn ngoài migrations hoặc là chạm vào database của bạn.<br> <br>

Bây giời, chạy lại migrate để tạo các bảng mô hình trong cơ sở dữ liệu của bạn.<br> <br>

Câu lệnh migrate nhận tất cả migrations nà nó chưa được nhận và chaỵ chúng lại lần nữa - về cơ bản bản, đồng bộ hóa các sự thay đổi của bạn trong mô hình với các thực thể trong cơ sở dữ liệu.<br> <br>

Migration rất là huữ dụng và để bạn thay đổi cho mô hình của bạn bất cứ lúc nào, như bạn phát triển phần mềm của bạn, ngoài ra có thể xóa cở sở dữ liệu của bản hoặc là một bảng và làm mới nó- nó chuyên về cập nhập cơ sở dữ liệu của bạn, mà không làm mất dữ liệu. Chúng tôi sẽ trình bày sâu hơn về chúng trong phần sau của hướng dẫn, nhưng hiện tại, hãy nhớ hướng dẫn ba bước để thực hiện thay đổi mô hình:<br> <br>
<b><li> Thay đổi mô hình (ở file model.py).</b>

<b><li> Chạy <code>pyhton manage.py makemigrations </code>để tạo migration cho sự việc thay dổi của chúng.</b>

<b><li> Chạy <code>pyhton manage.py migrate</code> để áp dúng các thay đổi từu database.</b><br><br>

Vấn đề mà các câu lệnh được chia ra để tạo và áp dụng mỉgrations là bởi vì khi bạn phải hoàn thành migrations cho phiên bản hệ thống điều khiển của bạn và chuyển chúng tới ứng dụng của ban; nó ko chỉ giúp bạn phảt triền dễ dàng mà còn hữu dụng cho nhiều thứ phát triển khác và ở trong sản phẩm.

Đọc <a href = "https://docs.djangoproject.com/en/4.0/ref/django-admin/">django-admin documentation</a> cho đủ thông tin về manage.py cho tới khi bạn dùng.


<h2> SỬ dụng với API </h2 >

Bây giờ, hãy đi vào tương tác với shell Python và quậy 1 tý với fre API Django cho bạn. Để tránh shell Pyhton, chúng ta sử dụng càu lệnh:

<center><code>python manage.py shell</code></center>

Chúng ta sử dụng thay thế loại đơn giản của pyhton, bởi vì <b>manage.py</b> thiết lập biến môi trường của <a href = "https://docs.djangoproject.com/en/4.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE">DJANGO_SETTING_MODULE</a>, mà cho Django Pyhton tập trung vào dự án cua bạn.

Một khi bạn đã sử dụng shell,khám phá <a href = "https://docs.djangoproject.com/en/4.0/topics/db/queries/">database API</a>. Note: khi xong baì hướng dẫn này mình sẽ nghiên cứu về API database:
<p>--------------------------------------------------------------------------------------------------------------------------------------<br></p>
<code>from polls.models import Choice, Question #import the model classes we just wrote</code>
<br>#No questions are in the system yets.
<code>Qetion.objects.all()</code>
<QuerrySet []>
<br>
<p> # Create a new Question><br>
# Support for time zones is enabled in the default settings file, so<br>
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()<br>
# instead of datetime.datetime.now() and it will do the right thing.</p>
<code>from django.utils import timezone<br>q = Quetion(question_text="What 's a new",pub_date = timezone.now())</code>

</br></br>
<p># Save the object into the database. You have to call save() explicitly.</p>
<code>q.save()</code>

<br><br>
<p># Now it has an ID</p>
<code>q.id </code><br>
1
<br><br>
<p>#Access model filde values via Python atrribute<br></p>
<code>q.quesion_text</code><br>
"What 's a new"
<br><br>
<p># objects.all() displays all the questions in the database.<br></p>
<code>Question.objects.all()</code><br>
<p> QuerySet [Question: Question object (1)]</p>
<p>--------------------------------------------------------------------------------------------------------------------------------------<br></p>


Hãy đợi 1 vài phút QuerySet [Question: Question object (1)] không thật sự giúp ích trong viện nhận diện đối tượng đó. Hãy chỉnh lại mô hihh Question và Choice bằng việc thêm phương thức <b>hai dấu gạch dưới trước và sau str</b>.
 
 <table>
    <th>polls/models.py</th>
    <td><code><br>
from django.db import models<br>class Question(models.Model):<br>
    # ...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    def __str__(self):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        return self.question_text<br><br>
class Choice(models.Model):<br>
    # ...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    def __str__(self):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        return self.choice_text
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</code></td>
</table>

Tóm tắt lại lần sử dụng shell:
<ol>
<li> Gọi tới lớp Question và Choice tại polls/models.py
<li> Kiểm tr các đối tượng question có sẵn trong database: Question.objects.all()
<li> Dùng phương thực objects.fillter(id =1) để lấy object có id =1. Fillter() dùng để tìm kiếm và trả về 1 object.
<li> Gọi class timezone ở django.utils
<li> Tìm kiếm các objects được tạo ra trong năm này bằng phương thức objects.get()và get sẽ trả về 1 list object thảo điều kiện. Lưu ý: thêm sau pub_date bằng 2 dấu gạch chân + thời gian nào đó (như là ngày: day, tháng: month, năm: year) nó sẽ so sánh thời gian thỏa điền kiện đó.
<li> Lấy object Question có giá trị id là 2 với phương thức get(id=2) và báo lỗi vì chưa có id nào bằng 2
<li> Như số 6 thay vì id =2 nó lấy id =1.
<li> Kiểm tra nó đã được tạo trong ngày hay không ( đây là phương thức ta vừa tạo ở trên).
<li> Tạo 1 biến q tập trung tới Question có id =1  với phương thức get().
<li> Kiểm tra Question có liên kết với Choice nào hay không. q.choice_set.all(). Điều này có thể nói Django đã tự động tạo ra phương thức với (tên mô hình liên kết + "_"+set và thêm dấu . để sử dụng phương thức).Với .all() nó trả về 1 list Choice liên kết với Question đó
<li> Tạo thêm 3 câu bình chọn bằng phương thức create() -Trả về Choice và tự lưu lại. Ở choice thứ 3 ta tạo c tham chiếu tới khi nó tạo thành câu câu bình chọn đó
<li> Choice có api truy cập tới Question bằng phương thức question
<li> Đếm số Choice đã được lưu bằng count
<li> Đếm số câu bằng .count
<li> Sử dụng Fillter để kiếm các các choice liên kết vơis question trong năm nay(Choice.Object.fillter(question__pub_data__year)) ở đây mình phân tích tham số truyền vào đầu tiên là tự động sinh ra biến với tên lớp liên kết viết bằng chữ thường thêm 2 dấu gạch dưới và tên biến và thêm 2 dấu gạch dưới và datetime muón xét.
<li> Cuối cùng chúng ta sẽ tìm kiếm câu hỏi bắt dầu từ và xóa nó. Ta tham chiếu c với q.choice_set.fillter(choice_text__startswith). Mình sẽ phân tích starts with nhiều từ bắt đầu từ. Khi nó trả về choice thì mình delete từng phần tử nó là được.
</ol>

Chú ý:
<li> Khi tạo chúng ta class kế thừa models.Model thì nó sinh ra phương thức Object và tự động thêm các phương thức như là <b>save(): để lưu; get(): dùng để ánh xạ tới 1 list hoặc 1 object với theo điều kiện của các tham số đưa vào; delete() dùng để xóa ngoài ra nó còn tự động xóa các dữ liệu liên kết với nó; count dùng để thống kê số lượng object. </b> 
<li>Ngoài ra chúng còn tự động các mô hình liên kết theo cấu trúc sau ("tên class liên kết viết bằng chữ thường"+ d2 dấu gạch chân +set).

Còn nhiều thông tin trong quan hệ mô hình, xem <a href = "https://docs.djangoproject.com/en/4.0/ref/models/relations/">try cập quan hệ các đối tượng </a>. Để biết thêm về cách sử dụng dấu gạch dưới kép để thực hiện tra cứu trường qua API, hãy xem <a href = "https://docs.djangoproject.com/en/4.0/topics/db/queries/#field-lookups-intro">Tra cứu trường</a>. Để biết chi tiết đầy đủ về API cơ sở dữ liệu, hãy xem<a href = " https://docs.djangoproject.com/en/4.0/topics/db/queries/"> tài liệu tham khảo API cơ sở dữ liệu</a> của chúng tôi.


<h2>Giới thiệu django admin</h2>

<h3>Tạo 1 tài khoảng admin</h2>

Trước tiên chúng ta cần tạo 1 user mà có thể đăng nhập vào trang admin. Chạy theo dòng lệnh dưới đấy:

<center><code>python manage.py createsuperuser</code></center>

Nhập tên đăng nhập user rồi ấn enter:

<center><code>Username: admin</code></center>

Sau đó, bạn sẽ được nhắc nhập địa chỉ email mong muốn của mình:

<center><code>Email address: admin@example.com</code></center>

Cuối cùng là bạn nhập mật khẩu. Bạn sẽ được hỏi lại mật khẩu lần 2 để xác nhân mật khẩu của bạn.


Các phần sau mình sẽ cập nhập sau các bạn có thể ngồi đọc trên link này: https://docs.djangoproject.com/en/4.0/intro/tutorial02/.


Sau khi kết thúc bài 2 chúng ta đã hiểu quy trình tạo một mô hình, ngoài ra chúng ta hiểu thêm về thuật ngữ migration, các kích hoạt các mô hình, API databases

--------------------------------------------

<h1>BÀI HỌC SỐ 3</h1>

Sau khi kết thúc bài 2 chúng ta đã có mô hình bây giờ chúng ta tập trung giao diện web "views".


<h2>Tổng quan bài học</h2>


view là một loại của trang web trong ứng dụng django của bạn mà thường phục vụ một chức năng cụ thể và có một mẫu cụ thể: Ví dụ ở một trang blog chúng ta có một số view như sau:
<ul>
<li> trang chủ blog- Hiện thị vài mục mới nhất.

<li> Trang nhập - trang liên kết cố định cho một mục nhập duy nhất.

<li> Trang dữ liệu trên năm - hiển thị tất cả các tháng với các mục nhập trong năm nhất định.

<li> Trang dữ liệu trên tháng - hiển thị tất cả các tháng với các mục nhập trong tháng nhất định.

<li> Trang dữ liệu trong - hiển thị tất cả các tháng với các mục nhập trong ngày nhất định.

<li> Hành đông bình luận - xử lý việc đăng nhận xét cho một mục nhất định.  
</ul>

Ở trong ứng dụng bình chọn. Chúng ta có 4 views:

<ul>
<li> Trang index - Hiện thị các câu hỏi mới nhất.
<li> Trang detail - Hiện các câu hỏi với các câu trả lời tương ứng cẩu hỏi đó.
<li> Trang result - Hiện thị số lượt vote của từng câu  hỏi.
<li> Hành động vote- xử lý việc bỏ phiếu cho câu hỏi mình tham gia bỏ phiếu. 
</ul>

Ở django, trang web và các nội dung khác được vận chuyển bởi view. Mổi view đại diện cho một hàm Python, Django sẽ chọn view theo ví dụ yêu từ URL.

<h2>Viết một sô Views</h2>

Chúng ta thêm vào thư mục một vài view cho <b>polls/views.py</b>. Theo dòng code dưới đấy:
<table>

<td>

def detail(request, question_id):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    response = "You're looking at the results of question %s."
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    return HttpResponse(response % question_id)

def vote(request, question_id):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    return HttpResponse("You're voting on question %s." % question_id)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
</td>
</table>

Với các view mới chúng ta thêm url trong <b>polls/urls.py</b> bằng thêm bằng cách gọi hàm path():

<table>

<td>


from django.urls import path

from . import views

urlpatterns = [
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # ex: /polls/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     path('', views.index, name='index'),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # ex: /polls/5/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     path('<int:question_id>/', views.detail, name='detail'),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # ex: /polls/5/results/
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     path('<int:question_id>/results/', views.results, name='results'),
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
</td>
</table>

Hãy nhìn vào trong thanh tìm kiếm với, /polls/34/ nó sẽ chạy  hàm detail() với tham số id ta truyền vào là 34. Theo mình nhận xét: 

<center><code>path('<'int:question_id'>'/', views.detail, name='detail'),</code></center>

khi được gọi /polls/34 thì việc đầu tiên là nó sẽ kiểm trang url parttern xem có cái url mẫu không thì nó thấy int : question_id nó sẽ gán cho question_id = 34 sau đó nó gọi hàm truyền tới tham số request là đối HTTP request và question_id =34 và hàm kia xử lý và trả về view cho url.

<h2>Viết các view thật sự làm cái gì đó</h2>

Ở bài học 2 chúng ta đã làm quen các API Database. Chúng ta sẽ bắt đầu với index() view, sẽ show ra tất cả câu hỏi:

<table>

<td>


from django.http import HttpResponse

from .models import Question


def index(request):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    latest_question_list = Question.objects.order_by('-pub_date')[:5]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    output = ', '.join([q.question_text for q in latest_question_list])<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    return HttpResponse(output)<br>

<p># Leave the rest of the views (detail, results, vote) unchanged</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;
</td>
</table>


Tuy nhiên, có một vấn đề ở đây: thiết kế của trang được mã hóa cứng trong chế độ xem. Nếu bạn muốn thay đổi giao diện của trang, bạn sẽ phải chỉnh sửa mã Python này. Vì vậy, hãy sử dụng hệ thống mẫu của Django để tách thiết kế khỏi Python bằng cách tạo mẫu mà chế độ xem có thể sử dụng.

Đầu tiên, tạo một đường dẫn gọi là templates ở trong thư mục polls của bạn. Django sẽ xem các mẫu của bạn ở đây.

Cấu hính templates cho project của bạn mô tả django sẽ tải và trích render templates. Các cấu hình tệp cài đặc mặc định <b>DjangoTemplates</b> backend mà tùy chọn <b>APP_DIRS</b> đặt TRUE. Bằng quy ước <b>DjangoTemplates</b> tìm kiếm một tệp con ở mỗi <b>INSTALLED_APPS</b>

Cùng với thư mục <b>templates</b> bạn đã tạo từ trước, tạo một thư mục khác gọi là polls và cùng với    