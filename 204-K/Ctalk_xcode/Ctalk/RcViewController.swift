//
//  RcViewController.swift
//  Ctalk
//
//  Created by 林裕騰 on 2018/7/22.
//  Copyright © 2018年 SJTU. All rights reserved.
//

import UIKit
//var x = 0

class RcViewController: UIViewController {

    @IBAction func RcBut(_ sender: Any) {
        
            RcButO.setBackgroundImage(#imageLiteral(resourceName: "Group 21"), for: .normal)
        
    }
    @IBOutlet weak var RcButO: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
