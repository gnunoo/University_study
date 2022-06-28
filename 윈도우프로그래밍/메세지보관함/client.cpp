#include <windows.h>
#include <TCHAR.H>

LRESULT CALLBACK WndProc(HWND hwnd, UINT iMsg, WPARAM wParam, LPARAM lParam);

HINSTANCE hInst;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)
{
	HWND 	 hwnd;
	MSG 	 msg;
	WNDCLASS WndClass;
	WndClass.style = CS_HREDRAW | CS_VREDRAW;
	WndClass.lpfnWndProc = WndProc;
	WndClass.cbClsExtra = 0;
	WndClass.cbWndExtra = 0;
	hInst = hInstance;
	WndClass.hInstance = hInstance;
	WndClass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
	WndClass.hCursor = LoadCursor(NULL, IDC_ARROW);
	WndClass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
	WndClass.lpszMenuName = NULL;
	WndClass.lpszClassName = _T("Window Class Name");
	RegisterClass(&WndClass);
	hwnd = CreateWindow(
		_T("Window Class Name"),
		_T("Client Window"),
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		NULL,
		NULL,
		hInstance,
		NULL
	);
	ShowWindow(hwnd, nCmdShow);
	UpdateWindow(hwnd);
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return (int)msg.wParam;
}

#define IDC_BUTTON 100
#define IDC_EDIT   101
LRESULT CALLBACK WndProc(HWND hwnd, UINT iMsg,
	WPARAM wParam, LPARAM lParam)
{
	//HDC hdc;
	static HWND hButton, hEdit;
	TCHAR str[100];
	char cstr[100];
	int msgLen;

	static WSADATA wsadata;
	static SOCKET s;
	static SOCKADDR_IN addr = { 0 };

	switch (iMsg)
	{
	case WM_CREATE:
		hButton = CreateWindow(
			_T("button"),
			_T("확인"),
			WS_CHILD | WS_VISIBLE | BS_PUSHBUTTON,
			200,
			0,
			100,
			25,
			hwnd,
			(HMENU)IDC_BUTTON,
			hInst,
			NULL
		);
		hEdit = CreateWindow(
			_T("edit"),
			_T("여기에 채팅을 입력하세요!!!"),
			WS_CHILD | WS_VISIBLE | WS_BORDER | ES_MULTILINE,
			0,
			0,
			200,
			25,
			hwnd,
			(HMENU)IDC_EDIT,
			hInst,
			NULL
		);

		WSAStartup(MAKEWORD(2, 2), &wsadata);
		s = socket(AF_INET, SOCK_STREAM, 0);
		addr.sin_family = AF_INET;
		addr.sin_port = 20;
		addr.sin_addr.s_addr = inet_addr("127.0.0.1");
		if (connect(s, (LPSOCKADDR)&addr, sizeof(addr)) == -1) return 0;
		break;
	case WM_COMMAND:
		switch (LOWORD(wParam))
		{
		case IDC_BUTTON:
			GetDlgItemText(hwnd, IDC_EDIT, str, 100);
			msgLen = WideCharToMultiByte(CP_ACP, 0, str, -1, NULL, 0, NULL, NULL);
			WideCharToMultiByte(CP_ACP, 0, str, -1, cstr, msgLen, NULL, NULL);
			send(s, cstr,sizeof(cstr), 0);
			break;
		}
		break;
	case WM_DESTROY:
		closesocket(s);
		WSACleanup();
		PostQuitMessage(0);
		break;
	}
	return DefWindowProc(hwnd, iMsg, wParam, lParam);
}
