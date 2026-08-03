# Swift UIKit

## Metadata

- **ID:** 1597026
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Functions, Swift, Hard, UIkit
- **Skills:** Swift (Advanced)

## Summary

This multiple choice question evaluates functions, Swift, and UIKit concepts, ideal for senior-level roles. The problem requires determining the output of a code snippet involving application and scene lifecycle methods in a Swift app.

## Problem Statement

`"import UIKit
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions:
    [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        print(""AppDelegate: didFinishLaunchingWithOptions called"")
        return true
    }
}
@UIApplicationMain
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {
        print(""SceneDelegate: willConnectTo called"")
        guard let _ = (scene as? UIWindowScene) else { return }
    }
    func sceneDidBecomeActive(_ scene: UIScene) {
        print(""SceneDelegate: sceneDidBecomeActive called"")
    }
    func sceneWillEnterForeground(_ scene: UIScene) {
        print(""SceneDelegate: sceneWillEnterForeground called"")
    }
}
`
```

 

What is the output of the code snippet?

## Preview

"import UIKit
