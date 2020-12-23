# Easy Android (Reversing / Native, Hooking)

* Description

```
Do you know AOS? Click Me 77777 💰!!
Then I will give you FLAG!
```



원래 의도된 풀이는 후킹이라는 기술을 이용하는 방법인데 대부분의 풀이자가 77777번 오토클릭으로 해결했다.

디컴파일 해보면 버튼을 클릭할때마다 MainActivity.this.cnt라는 변수 값을 1씩 늘려주면서 77777번일 때 Native 함수 stringFromJNI()를 실행해 GOHACK{FLAG} FLAG에 해당 하는 값을 리턴해준다.

Native 함수 같은 경우는 RC4 암호화 방식을 이용하였다.

```java
package com.example.easyandroid;

import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    int cnt = 0;

    public native String stringFromJNI();

    static {
        System.loadLibrary("native-lib");
    }

    /* access modifiers changed from: protected */
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) R.layout.activity_main);
        final TextView count = (TextView) findViewById(R.id.count);
        ((Button) findViewById(R.id.button)).setOnClickListener(new OnClickListener() {
            public void onClick(View view) {
                MainActivity.this.cnt++;
                MainActivity mainActivity = MainActivity.this;
                if (mainActivity.chk(mainActivity.cnt)) {
                    TextView textView = count;
                    StringBuilder sb = new StringBuilder();
                    sb.append(MainActivity.this.getString(R.string.gohack1));
                    sb.append(String.valueOf(MainActivity.this.stringFromJNI()));
                    sb.append(MainActivity.this.getString(R.string.gohack2));
                    sb.append(BuildConfig.FLAVOR);
                    textView.setText(sb.toString());
                    Toast.makeText(MainActivity.this.getApplicationContext(), "Good Job!", 0).show();
                    return;
                }
                count.setText(String.valueOf(MainActivity.this.cnt));
            }
        });
    }

    public boolean chk(int a) {
        return this.cnt >= 77777;
    }
}
```



나의 풀이 같은 경우는 Frida라는 동적 도구를 이용해서 풀이를 진행했다. 

```

```

